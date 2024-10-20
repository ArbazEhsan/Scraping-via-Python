from tabula import read_pdf


df = read_pdf("file:///C:/Users/arbaz/Downloads/products%20table.pdf",pages="1")
print(df)
