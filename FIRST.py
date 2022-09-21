'''language = [
    {"language":"python", "framework": "django"},
    {"language":"Java", "framework":"spring"},
    {"language":"python", "framework":"fast api"},
    {"language":ruby",  "framework":"rails"},
    {"language":"java", "framework":"vaadin"},
    {"language":"ruby", "framework":"sinatra"},
    {"language":"python", "framework":"flask"},
    {"language":"Javascript", "framework":"react"},
    {"language":"javascript", "framework":"svelte"}
]
write a program to create a dictionary from the language list above , make the Programming language the key and the value will be a list of all the framework associated to a programming language.

example:
programming_language = {
    "python": ["flask", "django"],
    "javascript":["react","svelte"]
    "ruby":["rails"]
}'''


languages = [
    {"language": "python", "framework": "django"},
    {"language": "Java", "framework": "spring"},
    {"language": "python", "framework": "fast api"},
    {"language": "ruby",  "framework": "rails"},
    {"language": "java", "framework": "vaadin"},
    {"language": "ruby", "framework": "sinatra"},
    {"language": "python", "framework": "flask"},
    {"language": "Javascript", "framework": "react"},
    {"language": "javascript", "framework": "svelte"}
]

language_sorted = {}
for lang in languages:
    language = lang["language"].lower().strip()
    framework = lang["framework"].lower().strip()
    try:
        language_sorted[language].append(framework)
    except KeyError:
        language_sorted[language] = []
        language_sorted[language].append(framework)
print(f"programming_language = {language_sorted}")
