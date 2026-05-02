import { useState } from "react";

const BASE_URL = "http://127.0.0.1:8000";

function App() {
  const [complaints, setComplaints] = useState([]);
  const [title, setTitle] = useState("");
  const [status, setStatus] = useState("OPEN");
  const [query, setQuery] = useState("");
  const [loading, setLoading] = useState(false);

  // CREATE
  const createComplaint = async () => {
    setLoading(true);
    const res = await fetch(`${BASE_URL}/complaints`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ title, status }),
    });

    const data = await res.json();
    alert(`Created with priority: ${data.priority}`);
    setLoading(false);
    loadComplaints();
  };

  // LOAD
  const loadComplaints = async () => {
    setLoading(true);
    const res = await fetch(`${BASE_URL}/complaints`);
    const data = await res.json();
    setComplaints(data);
    setLoading(false);
  };

  // SEARCH
  const search = async () => {
    setLoading(true);
    const res = await fetch(`${BASE_URL}/complaints/search?query=${query}`);
    const data = await res.json();
    setComplaints(data);
    setLoading(false);
  };

  // FILTER
  const filter = async () => {
    setLoading(true);
    const res = await fetch(`${BASE_URL}/complaints/filter?status=${status}`);
    const data = await res.json();
    setComplaints(data);
    setLoading(false);
  };

  // UPDATE STATUS
  const updateStatus = async (id, newStatus) => {
    await fetch(`${BASE_URL}/complaints/${id}/status?status=${newStatus}`, {
      method: "PUT",
    });
    loadComplaints();
  };

  // DELETE (only works if backend has delete API)
  const deleteComplaint = async (id) => {
    await fetch(`${BASE_URL}/complaints/${id}`, {
      method: "DELETE",
    });
    loadComplaints();
  };

  return (
    <div style={styles.container}>
      <h1 style={styles.heading}>Complaint Dashboard</h1>

      {/* CREATE */}
      <div style={styles.card}>
        <h3>Create Complaint</h3>
        <input
          placeholder="Title"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          style={styles.input}
        />

        <select
          value={status}
          onChange={(e) => setStatus(e.target.value)}
          style={styles.input}
        >
          <option>OPEN</option>
          <option>IN_PROGRESS</option>
          <option>RESOLVED</option>
          <option>CLOSED</option>
        </select>

        <button onClick={createComplaint} style={styles.button}>
          Create
        </button>
      </div>

      {/* SEARCH */}
      <div style={styles.card}>
        <input
          placeholder="Search..."
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          style={styles.input}
        />
        <button onClick={search} style={styles.button}>Search</button>
        <button onClick={filter} style={styles.button}>Filter</button>
        <button onClick={loadComplaints} style={styles.button}>Load All</button>
      </div>

      {/* LOADING */}
      {loading && <p>Loading...</p>}

      {/* LIST */}
      {complaints.map((c) => (
        <div key={c.id} style={styles.card}>
          <h3>{c.title}</h3>
          <p>Status: {c.status}</p>
          <p style={styles[c.priority]}>Priority: {c.priority}</p>

          {/* UPDATE */}
          <select onChange={(e) => updateStatus(c.id, e.target.value)}>
            <option>Update Status</option>
            <option>IN_PROGRESS</option>
            <option>RESOLVED</option>
            <option>CLOSED</option>
          </select>

          {/* DELETE */}
          <button onClick={() => deleteComplaint(c.id)} style={styles.delete}>
            Delete
          </button>
        </div>
      ))}
    </div>
  );
}

const styles = {
  container: {
    padding: 20,
    background: "linear-gradient(135deg, #1e3c72, #2a5298)",
    minHeight: "100vh",
    color: "white",
  },
  heading: { textAlign: "center" },
  card: {
    background: "rgba(255,255,255,0.15)",
    padding: 20,
    margin: "10px 0",
    borderRadius: 10,
  },
  input: {
    padding: 10,
    margin: 5,
  },
  button: {
    padding: 10,
    margin: 5,
    background: "#00c6ff",
    border: "none",
    color: "white",
    cursor: "pointer",
  },
  delete: {
    padding: 10,
    margin: 5,
    background: "red",
    border: "none",
    color: "white",
    cursor: "pointer",
  },
  HIGH: { color: "red" },
  MEDIUM: { color: "orange" },
  LOW: { color: "lightgreen" },
};

export default App;