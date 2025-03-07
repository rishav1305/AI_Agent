from crawl4ai.extraction_strategy import JsonCssExtractionStrategy

# Generate a schema (one-time cost)
html = "<div class='product'><h2>Gaming Laptop</h2><span class='price'>$999.99</span></div>"

schema = JsonCssExtractionStrategy.generate_schema(
    html,
    llm_provider="llama3.2",  # Open source alternative
    api_token=None,  # Not needed for Ollama
    base_url= "http://localhost:11434/v1",
)

# Use the schema for fast, repeated extractions
strategy = JsonCssExtractionStrategy(schema)