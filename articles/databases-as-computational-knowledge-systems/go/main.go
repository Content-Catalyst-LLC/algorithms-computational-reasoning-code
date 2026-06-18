package main
import "fmt"
func schemaQuality(fields, keys, constraints, metadata, lineage float64) float64 { return 100*(0.22*fields + 0.20*keys + 0.20*constraints + 0.20*metadata + 0.18*lineage) }
func main(){ fmt.Printf("test_name,value\nschema_quality_score,%.3f\n", schemaQuality(.90,.85,.80,.88,.82)) }
