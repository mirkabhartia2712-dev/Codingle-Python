import pandas as pd 
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from textblob import TextBlob 
from colorama import init, Fore
import time
import sys


init(autoreset=True)


def load_data(file_path='imbd_top_1000.csv'):
    try:
        df = pd.read_csv(file_path)
        df['combined_features'] = df['Genre'].fillna('') + '' + df['Overview'].fillna ('')
        return df
    except FileNotFoundError:
        print (Fore.RED + f"Error: The file '{file_path}' was not found.")
        exit()

movies_df = load_data()


tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies_df['combined_features'])
consine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)


def list_genres(df):
    return sorted(set(genre.strip() for sublist in df['Genre'].dropna().str.split(',') for genre in sublist))

genres = list_genres(movies_df)


def recommend_movies(genre=None, mood=None, rating=None, top_n=5):
    filtered_df = movies_df
    if genre:
        filtered_df = filtered_df[filtered_df['Genre'].str.contains(genre, case=False, na=False)]
    if rating:
        filtered_df = filtered_df[filtered_df['IMBD_Rating'] >= rating]
    filtered_df = filtered_df.sample(frac=1).reset_index(drop=True)


    recommendations = []
    for idx, row in filtered_df.iterrows():
        overview = row['Overview']
        if pd.isna(overview):
            continue
        polarity = TextBlob(overview).sentiment.polarity
        
        # Match mood based on sentiment polarity
        if mood == 'happy' and polarity < 0.2:
            continue
        elif mood == 'sad' and polarity > -0.1:
            continue
        elif mood == 'intense' and abs(polarity) < 0.3:
            continue
        
        recommendations.append({
            'Title': row['Series_Title'],
            'Genre': row['Genre'],
            'Rating': row['IMDB_Rating'],
            'Overview': overview,
            'Sentiment': 'Positive' if polarity > 0 else 'Negative' if polarity < 0 else 'Neutral',
            'Year': row['Released_Year']
        })
        
        if len(recommendations) >= top_n:
            break
    
    return recommendations


def ai_based_recommendations(movie_title, top_n=5):
    if movie_title not in movies_df['Series_Title'].values:
        return None
    
    idx = movies_df[movies_df['Series_Title'] == movie_title].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:top_n+1]  # Exclude the movie itself
    
    movie_indices = [i[0] for i in sim_scores]
    recommendations = []
    
    for i in movie_indices:
        row = movies_df.iloc[i]
        overview = row['Overview']
        polarity = TextBlob(overview).sentiment.polarity if pd.notna(overview) else 0
        
        recommendations.append({
            'Title': row['Series_Title'],
            'Genre': row['Genre'],
            'Rating': row['IMDB_Rating'],
            'Overview': overview,
            'Sentiment': 'Positive' if polarity > 0 else 'Negative' if polarity < 0 else 'Neutral',
            'Year': row['Released_Year']
        })
    
    return recommendations


def display_movie(movie, index):
    print(f"\n{Fore.CYAN}{'='*60}")
    print(f"{Fore.YELLOW}#{index} - {movie['Title']} ({movie['Year']})")
    print(f"{Fore.GREEN}Genre: {movie['Genre']}")
    print(f"{Fore.MAGENTA}IMDB Rating: {movie['Rating']}/10")
    print(f"{Fore.BLUE}Sentiment: {movie['Sentiment']}")
    print(f"{Fore.WHITE}Overview: {movie['Overview'][:200]}...")
    print(f"{Fore.CYAN}{'='*60}")


def animate_text(text, color=Fore.WHITE):
    for char in text:
        sys.stdout.write(color + char)
        sys.stdout.flush()
        time.sleep(0.02)
    print()


def main():
    animate_text("🎬 Welcome to the AI-Powered Movie Recommendation System! 🎬", Fore.CYAN)
    
    while True:
        print(f"\n{Fore.YELLOW}{'='*60}")
        print(f"{Fore.GREEN}Choose your recommendation method:")
        print(f"{Fore.WHITE}1. Browse by Genre")
        print(f"{Fore.WHITE}2. Find by Mood")
        print(f"{Fore.WHITE}3. Filter by IMDB Rating")
        print(f"{Fore.WHITE}4. AI-Based (Similar Movies)")
        print(f"{Fore.WHITE}5. Random Surprise")
        print(f"{Fore.WHITE}6. Exit")
        print(f"{Fore.YELLOW}{'='*60}")
        
        choice = input(f"\n{Fore.CYAN}Enter your choice (1-6): {Fore.WHITE}")
        
        if choice == '1':
            print(f"\n{Fore.GREEN}Available Genres:")
            for i, genre in enumerate(genres, 1):
                print(f"{Fore.WHITE}{i}. {genre}", end="  ")
                if i % 5 == 0:
                    print()
            print()
            
            genre = input(f"\n{Fore.CYAN}Enter genre name: {Fore.WHITE}")
            animate_text(f"\n🔍 Searching for {genre} movies...", Fore.YELLOW)
            results = recommend_movies(genre=genre)
            
        elif choice == '2':
            print(f"\n{Fore.GREEN}Select your mood:")
            print(f"{Fore.WHITE}1. Happy (uplifting, positive)")
            print(f"{Fore.WHITE}2. Sad (emotional, dramatic)")
            print(f"{Fore.WHITE}3. Intense (thrilling, action-packed)")
            
            mood_choice = input(f"\n{Fore.CYAN}Enter mood (1-3): {Fore.WHITE}")
            mood_map = {'1': 'happy', '2': 'sad', '3': 'intense'}
            mood = mood_map.get(mood_choice, 'happy')
            
            animate_text(f"\n🎭 Finding {mood} movies...", Fore.YELLOW)
            results = recommend_movies(mood=mood)
            
        elif choice == '3':
            rating = float(input(f"\n{Fore.CYAN}Enter minimum IMDB rating (e.g., 8.0): {Fore.WHITE}"))
            animate_text(f"\n⭐ Finding movies rated {rating}+...", Fore.YELLOW)
            results = recommend_movies(rating=rating)
            
        elif choice == '4':
            movie_title = input(f"\n{Fore.CYAN}Enter a movie you like: {Fore.WHITE}")
            animate_text(f"\n🤖 AI is analyzing similar movies...", Fore.YELLOW)
            results = ai_based_recommendations(movie_title)
            
            if results is None:
                print(f"{Fore.RED}Movie not found in database. Please try another title.")
                continue
                
        elif choice == '5':
            animate_text("\n🎲 Picking a random surprise for you...", Fore.YELLOW)
            results = recommend_movies(top_n=1)
            
        elif choice == '6':
            animate_text("\n👋 Thank you for using our system! Enjoy your movies! 🍿", Fore.CYAN)
            break
            
        else:
            print(f"{Fore.RED}Invalid choice! Please try again.")
            continue
        
        # Display results
        if results:
            print(f"\n{Fore.GREEN}✨ Found {len(results)} recommendation(s) for you!")
            for i, movie in enumerate(results, 1):
                display_movie(movie, i)
        else:
            print(f"\n{Fore.RED}❌ No movies found matching your criteria.")
        
        input(f"\n{Fore.CYAN}Press Enter to continue...")


if __name__ == "__main__":
    main()
    