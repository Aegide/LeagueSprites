import os

begin_html = """
<!DOCTYPE html>
<title>Champions sprites - Pokemon Showdown!</title>
<meta charset="utf-8" />
<style type="text/css">
html {
  background: #EEE;
  font: 12pt Verdana, sans-serif;
}
h1, h2, p {
  max-width: 800px;
  margin-left: auto;
  margin-right: auto;
}
figure {
	width: 96px;
	display: inline-block;
	vertical-align: top;
	text-align: center;
	margin: 0.5em 10px;
	overflow-wrap: break-word;
}
figure figcaption {
	font-size: 12px;
	text-align: center;
}
a {
	text-decoration: none;
}
a:hover {
	text-decoration: underline;
}
</style>
<h1><a href="http://www.pokemonshowdown.com">Pok&eacute;mon Showdown</a></h1>
<h2>Trainer sprites</h2>
"""

champion_html = """
<figure id="@.png">
<img src="@.png" alt="@.png" title="@.png" />
<figcaption><a href="@.png">@</a></figcaption>
</figure>
"""

# Clean index.html
index = open("index.html", "w")
index.write("")
index.close()

# Begin index.html
index = open("index.html", "a")
index.write(begin_html)

# Fill by champion
files = [f for f in os.listdir('.') if os.path.isfile(f) and f.endswith(".png")]
for f in files:
    champion = f.split(".")[0]
    index.write(champion_html.replace("@", champion))

# The END
index.close()