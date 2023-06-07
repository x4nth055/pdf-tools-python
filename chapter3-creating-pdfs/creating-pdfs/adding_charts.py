# adding_charts.py
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.graphics import renderPDF
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics.shapes import Drawing, String
from reportlab.lib.colors import HexColor

def add_custom_bar_chart(pdf_path):
    c = canvas.Canvas(pdf_path, pagesize=letter)
    width, height = letter

    # Create a Vertical Bar Chart object
    bar_chart = VerticalBarChart()
    # Set the size of the chart
    bar_chart.width = width - 200
    bar_chart.height = height - 300

    # Set the data for the chart
    data = [
        (10, 20, 30, 40, 50),  # series 1
        (15, 25, 35, 45, 55),  # series 2
    ]
    bar_chart.data = data

    # Set the labels for the x-axis
    bar_chart.categoryAxis.categoryNames = ['2019', '2020', '2021', '2022', '2023']

    # Set colors for each data series
    bar_chart.bars[0].fillColor = HexColor('#0D47A1')  # Dark Blue
    bar_chart.bars[1].fillColor = HexColor('#42A5F5')  # Light Blue

    # Add y-axis labels
    bar_chart.valueAxis.valueMin = 0
    bar_chart.valueAxis.valueMax = 60
    bar_chart.valueAxis.valueStep = 10
    bar_chart.valueAxis.labels.fontSize = 10
    bar_chart.valueAxis.labelTextFormat = '%d million USD'

    # Draw the chart on a Drawing object
    d = Drawing(0, 0)

    # Add a title with bold font
    title = String(width / 2 - 150, bar_chart.height + 50, 'Company Revenues (2019-2023)', fontSize=20)
    d.add(title)

    d.add(bar_chart)

    # Render the chart on the canvas
    renderPDF.draw(d, c, 50, 50)  # moved chart to bottom

    c.save()


add_custom_bar_chart("custom_bar_chart.pdf")
