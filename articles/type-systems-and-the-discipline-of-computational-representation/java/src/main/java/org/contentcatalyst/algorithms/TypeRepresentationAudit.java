package org.contentcatalyst.algorithms;

public class TypeRepresentationAudit {
  enum PublicationStatus { DRAFT, REVIEW, PUBLISHED, ARCHIVED }
  record ArticleRecord(String title, String slug, PublicationStatus status) {}

  public static void main(String[] args) {
    ArticleRecord record = new ArticleRecord(
      "Type Systems and the Discipline of Computational Representation",
      "type-systems-and-the-discipline-of-computational-representation",
      PublicationStatus.PUBLISHED
    );
    System.out.println("title,slug,status");
    System.out.println(record.title() + "," + record.slug() + "," + record.status());
  }
}
