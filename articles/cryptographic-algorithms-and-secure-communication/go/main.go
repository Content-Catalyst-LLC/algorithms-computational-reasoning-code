package main

import (
	"crypto/hmac"
	"crypto/sha256"
	"encoding/base64"
	"fmt"
)

func tag(message string, key []byte) string {
	mac := hmac.New(sha256.New, key)
	mac.Write([]byte(message))
	return base64.RawURLEncoding.EncodeToString(mac.Sum(nil))
}

func main() {
	key := []byte("educational-demo-key-32-bytes!!!!")
	message := "approved software update manifest"
	tampered := "tampered software update manifest"
	expected := tag(message, key)
	fmt.Printf("original verified=%v\n", hmac.Equal([]byte(tag(message, key)), []byte(expected)))
	fmt.Printf("tampered verified=%v\n", hmac.Equal([]byte(tag(tampered, key)), []byte(expected)))
}
