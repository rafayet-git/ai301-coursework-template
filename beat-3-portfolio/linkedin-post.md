I added two new security checks to an open source tool that scans AI assistant settings, and the project's maintainer merged them.

The tool is called mcp-audit. It reads the settings that AI assistants use to connect to other programs and warns when something is risky. It had no warning for programs launched in a container with full control of the host computer, so I wrote two rules: one rated high risk for the most dangerous settings, and one rated medium for host networking.

Before I submitted, I ran a checker I built, which I call a ship-gate, and it stopped me once for claiming proof I had not saved.

My ship-gate runs the project's own tests and then reads my pull request description against my evidence. My description said I had run three commands, but I had not saved their output. I saved it, corrected one phrase, and the gate passed. The maintainer's review then found one failing check, a test count in the docs that was out of date. I updated it the same day, and the rules merged.

What it taught me: back every claim with proof before someone else has to ask, and expect a reviewer to find what your own checks miss.

https://github.com/adudley78/mcp-audit/pull/259

#opensource #security #softwaretesting
