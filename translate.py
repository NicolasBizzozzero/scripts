import click
import googletrans


@click.command()
@click.argument("string")
@click.option("-s", "--source-language", default="fr", show_default=True,
              help="The language of the string passed as argument.")
@click.option("-d", "--destination-language", default="en", show_default=True,
              help=("The language in which you want the string to be "
                    "translated."))
@click.option("-D", "--detect-source", default=False, is_flag=True,
              show_default=True, help=("Try to detect the source language "
                                       "used."))
@click.help_option('-?', "-h", "--help")
@click.version_option(version="1.0.0")
def translate(string: str, source_language: str = "fr",
              destination_language: str = "en", detect_source: bool = False):
    """ Translate `string` from a source language to another language. """
    translator = googletrans.Translator()
    if detect_source:
        source_language = translator.detect(string)
    print(translator.translate(string, src=source_language,
                               dest=destination_language).text)


if __name__ == '__main__':
    translate()
