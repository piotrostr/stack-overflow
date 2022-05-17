package main

import (
	"context"
	"fmt"
	"log"
	"os"

	"github.com/aws/aws-sdk-go-v2/aws"
	"github.com/aws/aws-sdk-go-v2/config"
	"github.com/aws/aws-sdk-go-v2/service/s3"
)

func main() {
	path := "/Users/piotrostrowski/smplverse-api/artifacts/sample_face.png"
	file, err := os.OpenFile(path, os.O_RDONLY, os.FileMode(0o644))
	if err != nil {
		log.Fatal(err)
	}

	bucketName := "smplverse"
	key := "uploads"
	contentType := "image/png"
	cfg, err := config.LoadDefaultConfig(context.TODO())
	if err != nil {
		log.Fatal(err)
	}
	log.Printf("%+v\n", cfg)
	client := s3.NewFromConfig(cfg)

	// Upload the file to S3.
	uploadResp, err := client.PutObject(context.TODO(), &s3.PutObjectInput{
		Bucket:      aws.String(bucketName),
		Key:         aws.String(key),
		Body:        file,
		ContentType: aws.String(contentType),
	})
	if err != nil {
		log.Fatal(err)
	}
	fmt.Print(uploadResp)
}
