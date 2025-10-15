
import pyfiglet
from pyfiglet import Figlet

def list_fonts():
    return pyfiglet.FigletFont.getFonts()

def generate_ascii_art(text, font='standard'):
    try:
        fig = Figlet(font=font)
        return fig.renderText(text)
    except pyfiglet.FontNotFound:
        return "Font not found."

def main():
    print("Welcome to the ASCII Art Generator!")
    text = input("Enter the text to convert: ")

    print("\nAvailable fonts:")
    fonts = list_fonts()
    for i, font in enumerate(fonts):
        print(f"\n{i+1}. {font}")
        preview_text = font
        if len(preview_text) > 10:
            preview_text = preview_text[:10]
        
        try:
            ascii_preview = generate_ascii_art(preview_text, font)
            preview_lines = ascii_preview.split('\n')
            print('\n'.join(preview_lines))
        except Exception:
            print("    (Preview not available)")

    font_choice = input(f"\nEnter the number of the font you want to use (1-{len(fonts)}), or press Enter for default: ")

    if font_choice.isdigit() and 1 <= int(font_choice) <= len(fonts):
        font = fonts[int(font_choice)-1]
    else:
        font = 'standard'

    ascii_art = generate_ascii_art(text, font)
    print("\nGenerated ASCII Art:")
    print(ascii_art)

    save_to_file = input("Save to file? (y/n): ").lower()
    if save_to_file == 'y':
        file_name = input("Enter file name (e.g., ascii_art.txt): ")
        with open(file_name, 'w') as f:
            f.write(ascii_art)
        print(f"Saved to {file_name}")

if __name__ == "__main__":
    main()
