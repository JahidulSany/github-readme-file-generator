from generator import GithubReadmeGenerator
from data_instances import collect_content_data
from content_data import generate_content_data
from file_generate import generate_file

def main():
    # Create an instance of the GithubReadmeGenerator class
    readmeGenerator = GithubReadmeGenerator()

    # Collect content data from the user
    collect_content_data(readmeGenerator)

    # Generate the content for the README.md file
    content = generate_content_data(readmeGenerator)

    # Generate the README.md file with the generated content
    generate_file(readmeGenerator, content)

if __name__ == "__main__":
    main()
