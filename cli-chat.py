from main import ask, context

running = True
while running:
	# print("Context:", context)
	user_input = input("Ask: ")
	if user_input.startswith("/"):
		if user_input.lower() in ['/q', '/quit']:
			print("Bye...")
			running = False
			break
	ai_resonse = ask(user_input)
	print("AI :", ai_resonse)

