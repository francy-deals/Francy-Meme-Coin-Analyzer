import requests
import datetime

def check_solana_memecoins():
    print(f"=== Menjalankan Cek Meme Coin Solana pada {datetime.datetime.now()} ===")
    
    # Endpoint DexScreener untuk pencarian token Solana
    url = "https://api.dexscreener.com/latest/dex/search/?q=solana"
    
    try:
        response = requests.get(url)
        data = response.json()
        pairs = data.get("pairs", [])
        
        # Filter khusus jaringan Solana
        solana_pairs = [p for p in pairs if p.get("chainId") == "solana"]
        
        print(f"Ditemukan {len(solana_pairs)} token aktif di Solana:")
        for idx, pair in enumerate(solana_pairs[:5]):  # Ambil 5 teratas
            name = pair.get("baseToken", {}).get("name")
            symbol = pair.get("baseToken", {}).get("symbol")
            price_usd = pair.get("priceUsd")
            volume_h24 = pair.get("volume", {}).get("h24", 0)
            
            print(f"{idx+1}. {name} ({symbol}) | Harga: ${price_usd} | Vol 24h: ${volume_h24}")
            
    except Exception as e:
        print(f"Terjadi kesalahan saat mengambil data: {e}")

if __name__ == "__main__":
    check_solana_memecoins()
