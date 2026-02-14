# Serverless Rock–Paper–Scissors API on AWS

This project is a serverless REST API that implements the classic Rock–Paper–Scissors game using AWS Lambda and Amazon API Gateway. It was originally developed as part of a Cloud Architecture course and later refined to demonstrate practical knowledge of serverless computing, RESTful API design, and event-driven backend development in AWS.

## Project Overview

The objective of this project is to design and deploy a lightweight, scalable API that allows users to play Rock–Paper–Scissors through HTTP requests. When a client sends a POST request with their choice (`rock`, `paper`, or `scissors`), API Gateway receives and routes the request, AWS Lambda executes the game logic, a random choice is generated for the system, the winner is determined based on the game rules, and a structured JSON response is returned. The solution follows a stateless execution model and requires no server management.

## Architecture

Services used: AWS Lambda (serverless compute), Amazon API Gateway (REST endpoint), and Amazon CloudWatch (logging and monitoring). Architecture flow: Client → API Gateway → Lambda Function → JSON Response. The application is stateless, event-driven, automatically scalable, and operates under a pay-per-request model with fully managed infrastructure.

## Features

- Accepts user input (`rock`, `paper`, `scissors`)
- Randomized system selection
- Deterministic winner evaluation
- Structured JSON responses
- Deployed in AWS using serverless architecture
- Easily extendable to include persistence, authentication, CI/CD pipelines, or infrastructure as code

## API Endpoint

POST https://hy0gp41bt1.execute-api.us-east-2.amazonaws.com/playJokenpo

Headers:
Content-Type: application/json

Example request body:
{
  "user_choice": "rock"
}

Example response:
{
  "user_choice": "rock",
  "system_choice": "scissors",
  "result": "You win!"
}

## How to Test

Using Postman or a similar HTTP client: create a new POST request, add the endpoint URL, set the header `Content-Type` to `application/json`, provide a JSON body with the `user_choice`, send the request, and inspect the response.

## What This Project Demonstrates

- Practical experience with AWS serverless services
- REST API implementation and HTTP handling
- Backend business logic development
- Stateless architecture design
- Cloud-native application structure
- Basic observability through CloudWatch logs

This project can be expanded with automated testing (unit and integration tests), CI/CD pipelines (e.g., GitHub Actions), Infrastructure as Code (Terraform or CloudFormation), authentication and authorization layers, DynamoDB integration, or containerized deployment strategies.
