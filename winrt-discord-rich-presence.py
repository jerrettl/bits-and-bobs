#!/usr/bin/env python3
#
# Small proof-of-concept Python script that retrieves the currently-playing
# music from the Windows Runtime API, and display it to your Discord rich presence
# status. There is not much in the way of error handling, but *it just works*.
#
# Note that this script requires Python 3.10 or newer.
#
# Before running, you will need to create a developer application for Discord at
# https://discord.com/developers/ and copy your application ID to the
# `discord_application_id` variable.
#
# You will also need to install some extra libraries for working with the Windows
# Runtime API and Discord rich presence. For this, run:
#      pip install winsdk discord-rich-presence
#
# To use this, open Discord and run this script in a separate terminal.

import asyncio
import time

# https://github.com/pywinrt/pywinrt
# Run `pip install winsdk`.
from winsdk.windows.media.control import GlobalSystemMediaTransportControlsSessionManager as MediaManager
# https://github.com/TenType/discord-rich-presence
# Run `pip install discord-rich-presence`.
from discordrp import Presence

discord_application_id = "ADDMEHERE"


# Retrieve current media information from the Windows Runtime API.
# Sourced from: https://stackoverflow.com/questions/65011660/how-can-i-get-the-title-of-the-currently-playing-media-in-windows-10-with-python
async def get_media_info():
    sessions = await MediaManager.request_async()
    current_session = sessions.get_current_session()
    # Session must be valid.
    if current_session:
        info = await current_session.try_get_media_properties_async()
        return info


def main():
    # Connect to Discord.
    print("Connecting to Discord...")
    with Presence(discord_application_id) as presence:
        print("Connected to Discord! (Press Ctrl+C to quit.)")

        last_title = ""

        while True:
            print("Fetching current song information...")
            media_info = asyncio.run(get_media_info())
            title = media_info.title
            artist = media_info.artist

            # I listen to a lot of music from YouTube, and sometimes the
            # song is auto-processed by their system where the channel name
            # of the song is "<artist name> - Topic". We're just going to
            # take that out.
            if artist.endswith(" - Topic"):
                artist = artist.removesuffix(" - Topic")

            print(f"Title: {title}")
            print(f"Artist: {artist}")

            # Update Discord presence if the song has changed.
            if title != last_title:
                print("Updating Discord status...")

                # API details at: https://discord.com/developers/docs/topics/gateway-events#activity-object
                presence.set(
                    {
                        "details": f"Current Title: {title}",
                        "state": f"Artist: {artist}",
                    }
                )

                print("Discord status updated.")

            time.sleep(5)
            last_title = title

            print()

        print("Clearing presence!")
        presence.clear()

    print("Session closed.")


if __name__ == "__main__":
    main()
