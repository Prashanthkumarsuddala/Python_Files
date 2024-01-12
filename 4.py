def reverse_words(string):
  words = string.split(" ")
  reversed_words = words[::-1]
  reversed_string = " ".join(reversed_words)
  return reversed_string

if __name__ == "__main__":
  string = "Indur institute of engineering and technology siddipet"
  reversed_string = reverse_words(string)
  print(reversed_string)
