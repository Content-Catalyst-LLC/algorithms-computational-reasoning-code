export type PublicationStatus = "draft" | "review" | "published" | "archived";
export type ArticleRecord = {
  title: string;
  slug: string;
  series: "Algorithms & Computational Reasoning";
  status: PublicationStatus;
  repositoryUrl: string;
};

export const article: ArticleRecord = {
  title: "Type Systems and the Discipline of Computational Representation",
  slug: "type-systems-and-the-discipline-of-computational-representation",
  series: "Algorithms & Computational Reasoning",
  status: "published",
  repositoryUrl: "https://github.com/Content-Catalyst-LLC/algorithms-computational-reasoning-code/tree/main/articles/type-systems-and-the-discipline-of-computational-representation/"
};
