import { content } from "./content.js";

export default function Landing() {
  return (
    <div className="page">
      <nav>
        <span>{content.name}</span>
        <a href="/ask">Ask the assistant</a>
      </nav>
      <h1>{content.headline}</h1>
      <p className="intro">{content.intro}</p>
      <h2>What I do</h2>
      {content.skills.map((s) => (
        <div className="skill" key={s.title}>
          <strong>{s.title}</strong>
          <span>{s.note}</span>
        </div>
      ))}
      <a className="cta" href={content.contact.href}>{content.contact.label}</a>
    </div>
  );
}
