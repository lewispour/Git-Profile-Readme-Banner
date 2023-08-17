from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import random
from urllib.request import urlopen
import json


app = FastAPI()

@app.get("/api/python", response_class=HTMLResponse)
def root(
    username: str = None,
    bg: str = "#181818",
    fill: str = "#fff",
    avatar: str = True,
    txt: str = "A full-stack DevOps Engineer",
):

    if username is None or username == "":
        username = "LewisPour"
    if " " in username:
        html = """
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }

            body {
                font-family: 'Poppins', sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol";
                color: #fff;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                height: 100vh;
                background-color: #181818;
            }

            div {
                # font-size: 24px;
                padding: 4rem 2rem;
                background-color: #222323;
                border-radius: 5px;
                border: 1px solid #323233;
                text-transform: uppercase;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
            }

            button {
                font-family: inherit;
                text-transform: inherit;
                font-weight: 700;
                background-color: #3FCF8F;
                border: none;
                border-radius: 5px;
                padding: 1rem 2rem;
                color: #fff;
                font-size: 1.2rem;
                cursor: pointer;
                width: 100%;
            }

        </style>
        <div>
        <h1>Username cannot contain spaces</h1>
        <button onclick="window.location ='https://nextjs-fastapi-starter-iota-puce.vercel.app'">Help</button>
        </div>
        """
        return HTMLResponse(content=html, status_code=400)

    if bg == None or bg == "":
        bg = "#181818"

    if avatar != True:
        if avatar.lower() == "true" or avatar.lower() == "yes":
            avatar = True
        else:
            avatar = False

    if len(txt) > 63:
        txt = "The text should be less than or equal to 63 characters."

    github_url = "https://api.github.com/users/" + username
    with urlopen(github_url) as response:
        github_data = json.load(response)
    name = github_data["name"]


    colors = [
        "aliceblue",
        "antiquewhite",
        "aqua",
        "aquamarine",
        "azure",
        "beige",
        "bisque",
        "black",
        "blanchedalmond",
        "blue",
        "blueviolet",
        "brown",
        "burlywood",
        "cadetblue",
        "chartreuse",
        "chocolate",
        "coral",
        "cornflowerblue",
        "cornsilk",
        "crimson",
        "cyan",
        "darkblue",
        "darkcyan",
        "darkgoldenrod",
        "darkgray",
        "darkgreen",
        "darkgrey",
        "darkkhaki",
        "darkmagenta",
        "darkolivegreen",
        "darkorange",
        "darkorchid",
        "darkred",
        "darksalmon",
        "darkseagreen",
        "darkslateblue",
        "darkslategray",
        "darkslategrey",
        "darkturquoise",
        "darkviolet",
        "deeppink",
        "deepskyblue",
        "dimgray",
        "dimgrey",
        "dodgerblue",
        "firebrick",
        "floralwhite",
        "forestgreen",
        "fuchsia",
        "gainsboro",
        "ghostwhite",
        "gold",
        "goldenrod",
        "gray",
        "grey",
        "green",
        "greenyellow",
        "honeydew",
        "hotpink",
        "indianred",
        "indigo",
        "ivory",
        "khaki",
        "lavender",
        "lavenderblush",
        "lawngreen",
        "lemonchiffon",
        "lightblue",
        "lightcoral",
        "lightcyan",
        "lightgoldenrodyellow",
        "lightgray",
        "lightgreen",
        "lightgrey",
        "lightpink",
        "lightsalmon",
        "lightseagreen",
        "lightskyblue",
        "lightslategray",
        "lightslategrey",
        "lightsteelblue",
        "lightyellow",
        "lime",
        "limegreen",
        "linen",
        "magenta",
        "maroon",
        "mediumaquamarine",
        "mediumblue",
        "mediumorchid",
        "mediumpurple",
        "mediumseagreen",
        "mediumslateblue",
        "mediumspringgreen",
        "mediumturquoise",
        "mediumvioletred",
        "midnightblue",
        "mintcream",
        "mistyrose",
        "moccasin",
        "navajowhite",
        "navy",
        "oldlace",
        "olive",
        "olivedrab",
        "orange",
        "orangered",
        "orchid",
        "palegoldenrod",
        "palegreen",
        "paleturquoise",
        "palevioletred",
        "papayawhip",
        "peachpuff",
        "peru",
        "pink",
        "plum",
        "powderblue",
        "purple",
        "rebeccapurple",
        "red",
        "rosybrown",
        "royalblue",
        "saddlebrown",
        "salmon",
        "sandybrown",
        "seagreen",
        "seashell",
        "sienna",
        "silver",
        "skyblue",
        "slateblue",
        "slategray",
        "slategrey",
        "snow",
        "springgreen",
        "steelblue",
        "tan",
        "teal",
        "thistle",
        "tomato",
        "turquoise",
        "violet",
        "wheat",
        "white",
        "whitesmoke",
        "yellow",
        "yellowgreen",
    ]
    html = f"""
     <svg xmlns="http://www.w3.org/2000/svg" style='stroke-width: 0px; background-color: {bg};' width="700" height="185" viewBox="0 0 700 185" fill="{fill if fill[0] == "#" else fill if fill in colors else"#"+fill}" role="img">
        <title xmlns="http://www.w3.org/2000/svg">Lewis Pour's README</title>
         <desc>GitHub Profile Banner README Generator | Lewis Pour</desc>
         <desc>This API allows you to generate a dynamic image for your GitHub Profile README!</desc>
        {'<image href="https://github.com/lewispour/nextjs-fastapi-starter/blob/71b4976d84d149a18390f21463f0f144fcbe66c2/blackbackground.png" height="185"/>' if avatar else None}
        <style>
            * {{
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol";
                font-size: 18px;
                color: #fff;
                }}
            .head {{
                font-family: 'Poppins', sans-serif;
                font-size: 24px;
                font-weight: bold;
            }}

            tspan {{
                font-family: inherit;
                font-size: 24px;
                font-weight: 100;
                letter-spacing: -1px;
                text-transform: uppercase;
                fill: #3FCF8F;
                animation: change 1.5s ease-in-out infinite;
            }}

            @keyframes change {{
                0% {{
                    fill: #3FCF8F;
                    font-weight: bold;
                }}
                50% {{
                    fill: {random.choice(colors)};
                    font-weight: 100;
                }}
                100% {{
                    fill: #3FCF8F;
                    font-weight: bold;
                }}
            }}
            
        </style>
        <text x='{55 if avatar else 50}%' y='48%' class="head" text-anchor="middle">👋 Hey <tspan>&#60;Developers/&#62;</tspan>, I'm {name}!</text>
        <text x="{55 if avatar else 50}%" y="60%" class="subhead" text-anchor="middle">{txt}</text>
        
    </svg>
    """
    return HTMLResponse(
        content=html,
        media_type="image/svg+xml",
        headers={
            "Cache-Control": "no-cache, no-store, must-revalidate",
            "Pragma": "no-cache",
            "Expires": "0",
        },
    )
