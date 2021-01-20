import sys
import chevron
import datetime
from pathlib import Path

# List of all countries of interest
COUNTRIES = [
    "United Kingdom",
    "Australia",
    "United States",
    "Germany",
    "New Zealand",
    "Netherlands",
    "South Africa",
]

REQUIRED_PATHS = ["csv", "fig", "report"]


def convert_time(x):
    try:
        return datetime.datetime.strptime(str(x), "%Y-%m-%d %H:%M:%S").date()
    except ValueError:
        return x


def make_report(file):
    def inner_decorator(generator):
        def func(**kwargs):
            base = Path(file).stem
            year = int(Path(file).resolve().parent.stem) or datetime.datetime.utcnow().year()
            filename = base + ".md"
            template = first_existing(
                [Path("templates") / filename, Path("../templates") / filename]
            )
            if template is None:
                print("E: No template found for:", base)
                print("   Put a corresponding template in the appropriate folder")
                print("   For this year, in a 'template' subfolder of this folder")
                print("   For all years, in a 'template' subfolder of the parent folder")
                sys.exit(1)

            # Ensure these paths are present
            for p in map(Path, REQUIRED_PATHS):
                if not p.exists():
                    p.mkdir()

            report = generator(year=year, **kwargs)
            with template.open() as fp:
                (Path("report") / (filename)).write_text(chevron.render(fp, report))
            return report
        return func
    return inner_decorator


def table(name, data):
    csv = "csv/%s.csv" % name
    data.to_csv(csv, index=False)
    return {"t_" + name: data.to_markdown() + "\n\n[Download CSV](%s)" % ("../" + csv)}


def figure(name, plt):
    figpath = "fig/%s.png" % name
    plt.savefig(figpath)
    return {"f_" + name: "![%s](%s)" % (name, "../" + figpath)}


def first_existing(paths):
    for p in paths:
        if p.exists():
            return p
    return None
