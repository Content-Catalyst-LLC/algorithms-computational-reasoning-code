package main
import "fmt"
type PublicationStatus string
const Published PublicationStatus = "published"
type ArticleRecord struct { Title string; Slug string; Status PublicationStatus }
func main() {
	record := ArticleRecord{"Type Systems and the Discipline of Computational Representation", "type-systems-and-the-discipline-of-computational-representation", Published}
	fmt.Println("title,slug,status")
	fmt.Printf("%s,%s,%s\n", record.Title, record.Slug, record.Status)
}
