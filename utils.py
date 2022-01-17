import requests


def get_uniprot_sequence(protein_id: str) -> str:
    """
    Get the uniprot sequence for a given protein ID.
    """
    url = 'https://www.uniprot.org/uniprot/' + protein_id + '.fasta'
    response = requests.get(url)
    return ''.join(response.text.split('\n')[1:])
