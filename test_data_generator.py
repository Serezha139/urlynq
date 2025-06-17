import json
import random
import uuid


def generate_json_data(size=10000, max_friends=5):
    cities = [
        "Berlin", "Munich", "Hamburg", "Zurich", "Dusseldorf",
        "Frankfurt", "Stuttgart", "Cologne", "Leipzig", "Dresden",
        "Vienna", "Salzburg", "Geneva", "Basel", "Bern",
        "Paris", "London", "Rome", "Madrid", "Barcelona",
        "Lisbon", "Amsterdam", "Brussels", "Copenhagen", "Oslo",
        "Stockholm", "Helsinki", "Warsaw", "Prague", "Budapest",
        "Athens", "Istanbul", "Milan", "Naples", "Venice",
        "Bucharest", "Sofia", "Belgrade", "Zagreb", "Ljubljana",
        "Skopje", "Sarajevo", "Tirana", "Reykjavik", "Tallinn",
        "Riga", "Vilnius", "Luxembourg", "Monaco", "Andorra la Vella"
    ]
    professions = [
        "Engineer", "Artist", "Designer", "Developer", "Entrepreneur",
        "Teacher", "Scientist", "Musician", "Writer", "Photographer",
        "Architect", "Doctor", "Nurse", "Lawyer", "Accountant",
        "Chef", "Journalist", "Psychologist", "Marketing Specialist",
        "Sales Manager", "Project Manager", "Data Analyst", "Researcher",
        "Consultant", "Social Worker", "Veterinarian", "Pharmacist",
        "Civil Servant", "IT Specialist", "Web Developer", "Graphic Designer",
        "Software Engineer", "Business Analyst", "Financial Analyst",
        "Human Resources Manager", "Public Relations Specialist",
    ]

    places = [
        "Abu Dhabi", "Miami", "San Francisco", "Paris", "Tokyo", "New York City", "Bern", "Washington D.C.", "Hamburg",
        "London", "Sydney", "Cape Town", "Dubai", "Singapore", "Bangkok", "Rome", "Barcelona", "Moscow", "Istanbul",
        "Los Angeles", "Chicago", "Toronto", "Vancouver", "Rio de Janeiro", "Buenos Aires", "Mexico City", "Beijing",
        "Shanghai", "Hong Kong", "Seoul", "Mumbai", "Delhi", "Cairo", "Johannesburg", "Melbourne", "Auckland",
        "Lisbon", "Prague", "Vienna", "Amsterdam", "Brussels", "Stockholm", "Oslo", "Helsinki", "Copenhagen",
        "Warsaw", "Budapest", "Athens", "Dublin", "Edinburgh", "Venice"
    ]
    goals = [
        "Explore new cultures", "Develop new skills", "Exchange with other creators", "Find collaborators",
        "Connect with mentors / advisors", "Learn a new language", "Build a personal brand", "Start a business",
        "Improve physical fitness", "Master a musical instrument", "Write a book", "Create a portfolio",
        "Gain financial independence", "Volunteer for a cause", "Expand professional network", "Learn coding",
        "Become a mentor", "Achieve work-life balance", "Improve public speaking skills", "Learn photography",
        "Develop leadership skills", "Build a startup", "Create art", "Learn graphic design", "Study programming",
        "Become financially stable", "Travel to new places", "Visit new countries", "Understand digital tools",
        "Discover new hobbies", "Study IT", "Learn tech", "Explore technology", "Deepen industry knowledge",
        "Attend international conferences", "Create digital products", "Design a mobile app",
        "Mentor young professionals", "Publish online content", "Build a creative portfolio", "Host workshops",
        "Start a community", "Invest in startups", "Launch a podcast", "Create educational content",
        "Grow online presence", "Become an entrepreneur", "Found a startup", "Launch a company",
        "Take initiative", "Lead a team", "Get in shape", "Exercise regularly", "Boost physical health",
        "Explore the world", "Discover new cultures", "Become a leader", "Become a better communicator",
        "Enhance speaking skills", "Master communication", "Achieve money freedom", "Save and invest wisely",
        "Establish a public identity", "Promote yourself", "Make creative work", "Produce artwork",
        "Become an artist", "Understand code", "Become a developer", "Create content", "Design digital products",
        "Run workshops", "Teach others", "Coach beginners", "Travel for inspiration", "Work abroad",
        "Freelance globally", "Network with peers", "Build a remote career", "Speak at conferences",
        "Write blog posts", "Record video tutorials", "Create a YouTube channel", "Start a tech blog",
        "Publish a course", "Develop mobile games", "Work on open source", "Contribute to tech community",
        "Participate in hackathons", "Build a portfolio website", "Craft a design identity", "Create branding kits",
        "Learn app development", "Learn web development", "Learn database management", "Learn cloud computing",
        "Learn networking", "Learn system administration", "Learn ethical hacking", "Learn machine learning",
        "Learn data science", "Learn big data", "Learn IoT", "Learn quantum computing", "Learn bioinformatics",
        "Learn nanotechnology", "Learn renewable energy", "Learn environmental science", "Learn urban planning",
        "Learn architecture", "Learn civil engineering", "Learn mechanical engineering", "Learn electrical engineering",
        "Learn aerospace engineering", "Learn chemical engineering", "Learn biomedical engineering",
        "Learn materials science", "Learn geology", "Learn oceanography", "Learn meteorology", "Learn zoology",
        "Learn botany", "Learn ecology", "Learn genetics", "Learn microbiology", "Learn AI development",
        "Learn robotics", "Learn cybersecurity", "Build a SaaS product", "Develop a newsletter",
        "Launch an online brand",
        "Make digital illustrations", "Learn video editing", "Start a Twitch channel", "Create Instagram content",
        "Write poetry", "Publish a novel", "Start a fashion line", "Design sustainable products", "Make music",
        "Record an album", "Write a screenplay", "Make a short film", "Host events", "Organize local meetups",
        "Practice mindfulness", "Improve mental health", "Learn meditation", "Learn yoga", "Practice journaling",
        "Get better at time management", "Overcome procrastination", "Live more intentionally", "Support social causes",
        "Campaign for change", "Start a nonprofit", "Run for local office", "Create community spaces",
        "Promote diversity"
    ]

    fields_of_action = [
        "Education", "Tech", "Design", "Business", "Music", "Photography", "Art", "Modeling",
        "Healthcare", "Finance", "Marketing", "Sales", "Engineering", "Law", "Architecture",
        "Construction", "Real Estate", "Retail", "Hospitality", "Tourism", "Transportation",
        "Logistics", "Manufacturing", "Agriculture", "Energy", "Environment", "Telecommunications",
        "Media", "Entertainment", "Sports", "Gaming", "Publishing", "Advertising", "Public Relations",
        "Human Resources", "Consulting", "Research", "Development", "Nonprofit", "Government",
        "Military", "Aerospace", "Automotive", "Biotechnology", "Chemicals", "Consumer Goods",
        "Education Technology", "E-commerce", "Electronics", "Fashion", "Food and Beverage",
        "Healthcare Technology", "Insurance", "Investment Banking", "Legal Technology",
        "Luxury Goods", "Medical Devices", "Mining", "Oil and Gas", "Pharmaceuticals",
        "Private Equity", "Renewable Energy", "Retail Technology", "Robotics", "Semiconductors",
        "Social Media", "Software Development", "Space Exploration", "Sports Technology",
        "Supply Chain", "Textiles", "Transportation Technology", "Venture Capital",
        "Video Production", "Virtual Reality", "Water Management", "Web Development",
        "Wine and Spirits", "Writing", "Animation", "Game Design", "Cybersecurity",
        "Blockchain", "Artificial Intelligence", "Machine Learning", "Data Science",
        "Big Data", "Cloud Computing", "Internet of Things", "Quantum Computing",
        "Bioinformatics", "Nanotechnology", "Urban Planning", "Environmental Science",
        "Geology", "Oceanography", "Meteorology", "Zoology", "Botany", "Ecology",
        "Genetics", "Microbiology", "Astronomy", "Astrophysics", "Physics", "Chemistry",
        "Mathematics", "Statistics", "Economics", "Political Science", "Sociology",
        "Psychology", "Anthropology", "History", "Philosophy", "Linguistics"
    ]

    # Generate unique user IDs
    user_ids = [str(uuid.uuid4()) for _ in range(size)]

    # Track friendships to enforce mutual relationships
    friendships = {user_id: set() for user_id in user_ids}

    data = []
    for user_id in user_ids:
        # Generate friends for the current user
        potential_friends = [uid for uid in user_ids if uid != user_id]
        friends = random.sample(potential_friends, random.randint(0, max_friends))

        # Ensure mutual friendship
        for friend in friends:
            friendships[user_id].add(friend)
            friendships[friend].add(user_id)

    # Create user data
    for user_id in user_ids:
        item = {
            "_id": {"$oid": user_id},
            "name": f"User_{user_id[:8]}",
            "friends": list(friendships[user_id]),
            "hometown": random.choice(cities),
            "profession": random.choice(professions),
            "favoritePlacesToVisitString": random.sample(places, random.randint(1, 5)),
            "goalsString": random.sample(goals, random.randint(1, 2)),
            "professionalFieldsOfActionString": random.sample(fields_of_action, random.randint(1, 4)),
            "referralUserId": random.choice(user_ids)
        }
        data.append(item)
    return data


if __name__ == "__main__":
    json_data = generate_json_data()
    with open("generated_data_v3.json", "w") as file:
        json.dump(json_data, file, indent=4)