export type Status = "draft" | "review" | "published" | "archived";
export function transition(state: Status, requested: Status): Status {
  const allowed: Record<Status, Status[]> = { draft:["review"], review:["published","draft"], published:["archived"], archived:[] };
  return allowed[state].includes(requested) ? requested : state;
}
