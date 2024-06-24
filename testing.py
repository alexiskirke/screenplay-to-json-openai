from keys import KEY

# convert a screenplay
from screenplay_pdf_to_json import ScreenplayPDFToJSON
sptj = ScreenplayPDFToJSON(api_key=KEY)
data = sptj.convert('/Users/alexiskirke/Dropbox/Contracting/reader/screenplays/Severance_1x01_-_Mister.pdf')


# convert first 3 pages of a screenplay
from screenplay_pdf_to_json import ScreenplayPDFToJSON
sptj = ScreenplayPDFToJSON(api_key=KEY)
data2 = sptj.convert('/Users/alexiskirke/Dropbox/Contracting/reader/screenplays/drive-2011.pdf',
                     end_page=3)


# estimate cost of converting a screenplay
from screenplay_pdf_to_json import ScreenplayPDFToJSON
sptj = ScreenplayPDFToJSON(api_key=KEY)
cost = sptj.estimate_conversion_cost(
    '/Users/alexiskirke/Dropbox/Contracting/reader/screenplays/drive-2011.pdf')
print(f"Estimated cost to convert screenplay: ${cost:.2f}")


# convert first 3 pages of a screenplay which doesn't have a title page
from screenplay_pdf_to_json import ScreenplayPDFToJSON
sptj = ScreenplayPDFToJSON(api_key=KEY, skip_title_page=False)
data3 = sptj.convert('/Users/alexiskirke/Dropbox/Contracting/reader/screenplays/drive-2011.pdf',
                    end_page=3)