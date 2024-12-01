# editor-comma-counter
A web service in Python which provides the comma count in a provided string.

## Usage
First, build and run the service:

### Docker
- `docker build -t editor-comma-count .`
- `docker run -p 80:80 editor-comma-count`

### Directly
- `cd src/`
- `python main.py`

Then open `http://localhost:80/count_commas?text=your_text_here` in your favourite browser.