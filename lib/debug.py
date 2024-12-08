from models import Author, Magazine, Article

# Sample data for testing
# Create authors
author1 = Author("Alice")
author2 = Author("Bob")

# Create magazines
magazine1 = Magazine("Tech Daily", "Technology")
magazine2 = Magazine("Health Weekly", "Health")

# Create articles using authors and magazines
article1 = author1.add_article(magazine1, "AI Trends in 2024")
article2 = author1.add_article(magazine2, "Mental Health Awareness")
article3 = author2.add_article(magazine1, "Blockchain Basics")

# Debugging Section
print("Authors:")
print(f"Author 1: {author1.name}")
print(f"Author 2: {author2.name}")

print("\nMagazines:")
print(f"Magazine 1: {magazine1.name} - Category: {magazine1.category}")
print(f"Magazine 2: {magazine2.name} - Category: {magazine2.category}")

print("\nArticles:")
print(f"Article 1: {article1.title} - Author: {article1.author.name} - Magazine: {article1.magazine.name}")
print(f"Article 2: {article2.title} - Author: {article2.author.name} - Magazine: {article2.magazine.name}")
print(f"Article 3: {article3.title} - Author: {article3.author.name} - Magazine: {article3.magazine.name}")

print("\nTesting Methods:")

# Author Methods
print(f"{author1.name}'s Articles: {[article.title for article in author1.articles()]}")
print(f"{author1.name}'s Magazines: {[mag.name for mag in author1.magazines()]}")
print(f"{author1.name}'s Topic Areas: {author1.topic_areas()}")

# Magazine Methods
print(f"Articles in {magazine1.name}: {[article.title for article in magazine1.articles()]}")
print(f"Contributors to {magazine1.name}: {[author.name for author in magazine1.contributors()]}")

# Bonus Methods
try:
    top_publisher = Magazine.top_publisher()
    print(f"Top Publisher: {top_publisher.name}")
except Exception as e:
    print(f"Error determining top publisher: {e}")

# Start an interactive debugging session
import ipdb
ipdb.set_trace()
