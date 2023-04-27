import requests

url = 'https://httpbin.org/post'

data_transaksi = {
    'nama_pemilik':'Alberd Evelyn Ramadhan',
    'nomor_rekening': '9834502410',
    'kartu_expired_bulan': '12',
    'kartu_expired_tahun': '25',
    'kartu_cvv': '022',
    'pembayaran': 100.000,
    'mata_uang': 'Rupiah',
    'deskripsi': 'Pembayaran untuk produk Sepatu'
}
response = requests.post(url, json=data_transaksi)

if response.status_code == 200:
    print(response.text)
else:
    print(f"Error : {response.status.code}")
