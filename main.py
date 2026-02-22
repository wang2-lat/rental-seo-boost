import typer
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from seo_analyzer import analyze_seo_health
from local_seo import generate_local_seo_suggestions
from content_planner import generate_content_plan

app = typer.Typer(help="CLI tool to analyze and boost SEO for vacation rental websites")
console = Console()

@app.command()
def health_check(url: str):
    """Analyze SEO health of a vacation rental website"""
    console.print(f"\n[bold cyan]Analyzing SEO health for:[/bold cyan] {url}\n")
    
    results = analyze_seo_health(url)
    
    if "error" in results:
        console.print(f"[bold red]Error:[/bold red] {results['error']}")
        return
    
    table = Table(title="SEO Health Check Results")
    table.add_column("Metric", style="cyan")
    table.add_column("Status", style="magenta")
    table.add_column("Details", style="green")
    
    for metric, data in results.items():
        status = "✓" if data.get("passed", False) else "✗"
        table.add_row(metric, status, data.get("message", ""))
    
    console.print(table)
    console.print("\n[bold yellow]Recommendations:[/bold yellow]")
    for rec in results.get("recommendations", []):
        console.print(f"  • {rec}")

@app.command()
def local_seo(location: str, business_name: str):
    """Generate local SEO optimization suggestions"""
    console.print(f"\n[bold cyan]Generating local SEO suggestions for:[/bold cyan] {business_name} in {location}\n")
    
    suggestions = generate_local_seo_suggestions(location, business_name)
    
    console.print(Panel(suggestions["google_business"], title="Google Business Profile Setup", border_style="green"))
    console.print(Panel(suggestions["local_keywords"], title="Local Keywords to Target", border_style="blue"))
    console.print(Panel(suggestions["map_integration"], title="Map Integration Tips", border_style="yellow"))

@app.command()
def content_plan(property_type: str = "vacation rental", location: str = ""):
    """Generate content marketing plan"""
    console.print(f"\n[bold cyan]Generating content marketing plan...[/bold cyan]\n")
    
    plan = generate_content_plan(property_type, location)
    
    console.print(Panel(plan["blog_topics"], title="Blog Post Ideas", border_style="green"))
    console.print(Panel(plan["social_media"], title="Social Media Strategy", border_style="blue"))
    console.print(Panel(plan["review_strategy"], title="Customer Review Strategy", border_style="yellow"))

if __name__ == "__main__":
    app()
