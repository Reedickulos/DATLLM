from duckduckgo_search import DDGS

def search_web(query):
    """Returns the top DuckDuckGo result summary"""
    results = []
    with DDGS() as ddgs:
        for r in ddgs.text(query, max_results=3):
            results.append(f"- {r['title']}:\n  {r['body']}\n  [🔗] {r['href']}\n")
    if not results:
        return "No results found."
    return "\n".join(results)
