import { createRoot } from "react-dom/client";
import Landing from "./Landing.jsx";
import Ask from "./Ask.jsx";
import "./styles.css";

// Two pages, no router library: "/" is the landing page, "/ask" is the chat from Session 3.
const Page = window.location.pathname.startsWith("/ask") ? Ask : Landing;
createRoot(document.getElementById("root")).render(<Page />);
