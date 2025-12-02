import argparse
from rich import print
from core.validator import validate_number
from core.carrier_lookup import prefix_match
from core.osint_lookup import osint_lookup
from core.breach_checker import breach_check
from core.spam_checker import spam_check
from core.social_scan import social_scan

def run_mobiscope(number):
    print("[bold blue]\n[MOBISCOPE] Real-Time Phone Intelligence Scanner[/bold blue]")
    print("-------------------------------------------------------")

    info = validate_number(number)
    prefix = prefix_match(info["e164"])
    osint = osint_lookup(number)
    breach = breach_check(number)
    spam = spam_check(number)
    social = social_scan(number)

    print(f"[bold green]Number:[/bold green] {info['e164']}")
    print(f"[cyan]Valid:[/cyan] {info['valid']}")
    print(f"[cyan]Region:[/cyan] {info['region']}")
    print(f"[cyan]Carrier:[/cyan] {info['carrier']}")
    print(f"[cyan]Timezones:[/cyan] {info['timezones']}")
    
    if prefix:
        print(f"[cyan]Detected Country:[/cyan] {prefix['country']}")
        print(f"[cyan]Carrier Guess:[/cyan] {prefix['carrier_guess']}")

    print("\n[yellow]OSINT Summary:[/yellow]")
    print(osint)

    print("\n[yellow]Breach Check:[/yellow]")
    print(breach)

    print("\n[yellow]Spam Reputation:[/yellow]")
    print(spam)

    print("\n[yellow]Social Media Scan:[/yellow]")
    print(social)

    print("\n[green]Scan complete.[/green]")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("number", help="Phone number to scan")
    args = parser.parse_args()
    run_mobiscope(args.number)
