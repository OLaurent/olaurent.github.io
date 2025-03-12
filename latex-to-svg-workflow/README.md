# latex-to-svg-workflow

This project provides a workflow for converting LaTeX documents into SVG format. It automates the process of compiling a LaTeX file and converting the resulting DVI file to SVG, while also applying specific modifications to the generated SVG file.

## Project Structure

```
latex-to-svg-workflow
├── scripts
│   ├── convert_latex_to_svg.sh  # Shell script for LaTeX to SVG conversion
│   └── modify_svg.py             # Python script for modifying the SVG file
├── input
│   └── .gitkeep                  # Keeps the input directory in version control
├── output
│   └── .gitkeep                  # Keeps the output directory in version control
├── README.md                     # Documentation for the project
└── .gitignore                    # Specifies files to ignore in version control
```

## Setup

1. Ensure you have LaTeX and dvisvgm installed on your system.
2. Clone this repository to your local machine.

## Usage

1. Place your LaTeX file (e.g., `temporary.tex`) in the `input` directory.
2. Run the conversion script:

   ```bash
   ./scripts/convert_latex_to_svg.sh
   ```

3. This will generate an SVG file in the `output` directory.
4. The SVG file will be modified according to the specified requirements.

## Modifications to SVG

The `modify_svg.py` script performs the following modifications on the generated SVG file:

- Adds `style="display: block; margin: 0 auto;"` to the SVG tag.
- Replaces all occurrences of `#000` with `#3e8ed0`.
- Removes any paths that have the attribute `fill='#fff'`.
- Adds `fill:#3e8ed0;` in front of the `font-family` keyword.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.