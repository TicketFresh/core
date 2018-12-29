FROM python:3.4
ADD . /ticketfresh
WORKDIR /ticketfresh

# Install Dependencies
RUN pip install -r requirements.txt

# Run Flask Project
CMD ["python", "routes.py"]