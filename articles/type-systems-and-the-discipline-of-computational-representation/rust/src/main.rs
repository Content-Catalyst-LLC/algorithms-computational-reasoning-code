#[derive(Debug)]
enum PublicationStatus { Draft, Review, Published, Archived }

#[derive(Debug)]
struct ArticleRecord {
    title: String,
    slug: String,
    status: PublicationStatus,
}

fn valid_slug(slug: &str) -> bool {
    !slug.is_empty() && slug.chars().all(|c| c.is_ascii_lowercase() || c.is_ascii_digit() || c == '-')
}

fn main() {
    let article = ArticleRecord {
        title: "Type Systems and the Discipline of Computational Representation".to_string(),
        slug: "type-systems-and-the-discipline-of-computational-representation".to_string(),
        status: PublicationStatus::Published,
    };
    println!("valid_slug,{}", valid_slug(&article.slug));
    println!("article_title,{}", article.title);
}
