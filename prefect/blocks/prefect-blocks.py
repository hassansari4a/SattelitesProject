from prefect_gcp import GcpCredentials
from prefect_gcp.cloud_storage import GcsBucket

GCS_bucket_name = "sat_data_lake_idyllic-aspect-382707"  # insert your GCS bucket name
service_account_credentials = {
  "type": "service_account",
  "project_id": "idyllic-aspect-382707",
  "private_key_id": "5a12ada49463d060809a60225e5c5dc138c7fa80",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQDMS7bkx7d0jROy\nGx06Os1HTeL8Cm9YMBEBV5+7q1dPM7iMbdBxge04RhusYANFQGZ2ilSMvXTCm2Bq\nCGI4MhxsI+IvvkabngfWadAbZav3/XG+ePnG77ORdp6sS0hjhDQqi+UFLG9vRVng\nSso+i+Ze+XGU8nyplnqyE49DF8fSt53j1O5tdl6jLtT6pqljSF23gO5rhn4BiDCJ\n9iC9mNTDikw+XkYL0iVwBiqayEVmwdKhBHgBRQ4sd0LNiOKd/PSBn2lNkW/enmd4\nvF1yIl2s1Pzj/ad0COI8w/pRTfgsLmmFa2xH0hMsXWIyM7KP2BgNxttnNHeJWjHC\nsdJRr4+RAgMBAAECggEACLmnGwhIloq775xm2CjQwZ3a9ua/MKYE4+jJIqvDs9dC\np4S9JUvmRMQBxI/pM9j3R1LLH6Ory+/04zJud3X0bs3tiBp5S4YpUYf9Yl4qRRIm\n/HqQOGXeZnUJe9RPSCjKTZLh+iGWtMridsja8GbrNN00c6cTme6aWOaq9LOcTiyD\n2K6BJ3OWAMeQn9TR5NUWaaVATPuO/P6gQFfD2trzTm9WbxnOHihTe3Aq7F7ePaW+\nAGR/2t3WwgD9H7L1yGjMlV/e6PYZU+RfO4342z5tbGc6RqXuKDDKid3MsPxvSR6O\n4nmTQnQTTevnnsDfgLZJHWb9MlsjbrU+f3xR0llzDQKBgQDzDFX5UANZaPYfCQRA\n9BXNOTHMvJ6joNITMjx/wSoyR1ij+6jedjV7GdMplfnxuYduK2HbMS6KhoM+xPVn\nbxWq66o2GK0H3dNfY2c5rt8aDecCYJtUrPN4ooAMVDziV5r6+lYK5D+yC8sQ0ynV\nH9HqZKp1xM8kaPN80pRffDPhwwKBgQDXLrfFGhbJMgePIMmrgdt4jhI5Ktk4zoAJ\n3UHL6oYItBv+MazJivY9J0/H/TvXbNdH0d+vntF+0LBSoJO2JFUKpQHjGhffXF+N\nn5puAm++ptPCLziLG1L9nkI7ec7vF3LHn57HjGygyNdSUS7KudpK9Ow7zhVoLTw/\n+9a4jsJAGwKBgQCWLLManxPStQYOWxXjxG2MJqDcrlcfJ4lmDw5Oqd4WvvrIKAFJ\no6Sb8XMGKQMNFuPVcLzAIP1u3npN2IkBZiPvPjonvst7JtcqA1OO0rxLbvekAmk3\nwr2VdmLEO3B7MkIyfWeYxzuMGblZJgCdDVI5EAY7SmXrS2XXZI4FCctM3QKBgQCT\naeTpeZr8kHKPQhYGkbqp1yJy2YDgos8ictpdeTgDhGfc92j41WMlt+W3CyvQxDaj\ndAr6xCGe8BarNGidEjzUQwCM9VY/ZYfsfNeN38tv39gYIsNowPpU1vNmzWbPcs/m\nI9rht7i/WXfxY75bkYETcsDXo7IUoVCyQLPz0ZEP2wKBgQDnzUKwWNDfLJ+fjz6B\nfiefSQmf3NvHwyApyzppex6NJ7LlbKd1CPV2vgGOz6uGI4hTc9EklVT+AbpO/6Ez\nyY+jA2ziGgXk7NCcnlOQdwZYCrfeO8Y3yrM6LLpuO42mmUputIvO5OEMKSaTvIga\nq4S+4a3trtSKdrTOZ9KDqMatRA==\n-----END PRIVATE KEY-----\n",
  "client_email": "satuser@idyllic-aspect-382707.iam.gserviceaccount.com",
  "client_id": "117387893546449988333",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/satuser%40idyllic-aspect-382707.iam.gserviceaccount.com"
}



credentials_block = GcpCredentials(
    service_account_info= service_account_credentials
)
credentials_block.save("sat-gcp-credendials", overwrite=True)

bucket_block = GcsBucket(
    gcp_credentials=GcpCredentials.load("sat-gcp-credendials"),
    bucket=GCS_bucket_name,
)
bucket_block.save("satproject-storage-bucket", overwrite=True)