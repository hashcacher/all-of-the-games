# This script will parse the video game txt and make a JSON file structured the way our viz will use it
import re

def parse_video_games(game_file):
	for i, line in enumerate(game_file):
		m = re.match(r"(?P<title>.+) \((?P<alternatetitle>.+)\) \((?P<year>\d{4}), .+	 ", line)
		

		m = re.match(r"(.+?) (\((.+?)\))? \((\d{4}), .+	 ", line)
		

		m = re.match(r"(?P<title>.+) (\(.+\))?", line)

		if(m):
			print(m.group())
			# print(m.group('title'), m.group('alternatetitle'), m.group('year'))
		if i == 4:
			break

parse_video_games(open('allofthegames.txt'))