def recommend_clothing():
  """
  Prompts the user for weather conditions and provides clothing recommendations using if-else statements.
  """
  weather = input("What's the weather like today? (sunny/rainy/cold): ").lower()

  if weather == "sunny":
    recommendation = "Wear a t-shirt and sunglasses."
  elif weather == "rainy":
    recommendation = "Don't forget your umbrella and a raincoat."
  elif weather == "cold":
    recommendation = "Make sure to wear a warm coat and a scarf."
  else:
    recommendation = "Sorry, I don't have recommendations for this weather."

  print(recommendation)


if __name__ == "__main__":
  recommend_clothing()
