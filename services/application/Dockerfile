FROM python:3.4

# Copy necessary app files
ADD static /ticketfresh/static
ADD utilities /ticketfresh/utilities
COPY requirements.txt /ticketfresh
COPY routes.py /ticketfresh


# Switch to folder with all code in it
WORKDIR /ticketfresh

# Install Dependencies
RUN pip install -r requirements.txt

# Run Flask Project
CMD ["python", "routes.py"]