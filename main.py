from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import JSONFormatter

# Must be a single transcript.
# If the video language is in English, just remove the languages part below, or you can still specify it as 'en'.
transcript = YouTubeTranscriptApi.get_transcript("video_id", languages=['tr'])
# video_id is the part of the youtube video url just after v=
# example --> transcript = YouTubeTranscriptApi.get_transcript("B2xWkBWDsJY", languages=['tr'])

formatter = JSONFormatter()

# .format_transcript(transcript) turns the transcript into a JSON string.
json_formatted = formatter.format_transcript(transcript)


# Now we can write it out to a file.
with open('your_file_name.json', 'w', encoding='utf-8') as json_file:
    json_file.write(json_formatted)
# example
'''
with open('sample.txt.json', 'w', encoding='utf-8') as json_file:
    json_file.write(json_formatted)
'''
# Now should have a new JSON file that you can easily read back into Python.