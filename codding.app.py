
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Aplikasi Model Matematika Industri", layout="wide")

# Sidebar
st.sidebar.title("Dokumentasi Aplikasi")
st.sidebar.info(
    "Aplikasi ini terdiri dari tiga tab utama:\n"
    "1. Optimasi Produksi (Linear Programming)\n"
    "2. Model Persediaan (EOQ)\n"
    "3. Model Antrian (M/M/1)"
)

# Tabs
tab1, tab2, tab3 = st.tabs(["📈 Optimasi Produksi", "📦 Model Persediaan (EOQ)", "⏳ Model Antrian (M/M/1)"])

with tab1:
    st.header("📈 Optimasi Produksi: PT TechNova")
    st.write("PT TechNova memproduksi Laptop dan Tablet dengan sumber daya terbatas.")

    st.subheader("Fungsi Objektif")
    st.latex("Z = 500x + 300y")

    st.subheader("Kendala:")
    st.latex("4x + 2y \leq 160")
    st.latex("3x + y \leq 120")
    st.latex("x \geq 0, y \geq 0")

    st.subheader("Visualisasi Area Feasible")
    x_vals = np.linspace(0, 50, 400)
    y1 = (160 - 4*x_vals) / 2
    y2 = (120 - 3*x_vals)
    y_vals = np.minimum(y1, y2)
    y_vals = np.maximum(0, y_vals)

    fig, ax = plt.subplots()
    ax.plot(x_vals, y1, label="4x + 2y ≤ 160")
    ax.plot(x_vals, y2, label="3x + y ≤ 120")
    ax.fill_between(x_vals, 0, y_vals, where=(y_vals>=0), alpha=0.3)
    ax.set_xlabel("x (Laptop)")
    ax.set_ylabel("y (Tablet)")
    ax.legend()
    st.pyplot(fig)

with tab2:
    st.header("📦 Model Persediaan (EOQ): Toko KaryaTech")
    D = 6000  # Permintaan tahunan
    S = 75000  # Biaya pesan
    H = 5000  # Biaya simpan
    EOQ = np.sqrt(2 * D * S / H)

    st.write(f"Permintaan tahunan (D): {D} unit")
    st.write(f"Biaya pemesanan per order (S): Rp{S:,}")
    st.write(f"Biaya penyimpanan per unit per tahun (H): Rp{H:,}")
    st.subheader("Hasil Perhitungan EOQ")
    st.latex(f"EOQ = \sqrt{{\frac{{2 \times {D} \times {S}}}{{{H}}}}} = {EOQ:.2f}")
    st.success(f"Jumlah optimal pemesanan: {int(round(EOQ))} unit per pemesanan")

    st.subheader("Grafik Total Biaya")
    Q = np.arange(50, 500, 10)
    TC = (D / Q) * S + (Q / 2) * H
    fig2, ax2 = plt.subplots()
    ax2.plot(Q, TC, label="Total Cost")
    ax2.axvline(EOQ, color='r', linestyle='--', label=f"EOQ ≈ {int(round(EOQ))}")
    ax2.set_xlabel("Jumlah Pesanan (Q)")
    ax2.set_ylabel("Total Biaya (Rp)")
    ax2.legend()
    st.pyplot(fig2)

with tab3:
    st.header("⏳ Model Antrian (M/M/1): ServisPro")
    λ = 8  # rata-rata kedatangan per jam
    μ = 10  # rata-rata pelayanan per jam

    ρ = λ / μ
    L = ρ / (1 - ρ)
    W = 1 / (μ - λ)
    Wq = λ / (μ * (μ - λ))

    st.write(f"Rata-rata kedatangan (λ): {λ} pelanggan/jam")
    st.write(f"Rata-rata pelayanan (μ): {μ} pelanggan/jam")

    st.subheader("Hasil Analisis")
    st.write(f"Utilisasi Server (ρ): {ρ:.2f}")
    st.write(f"Jumlah pelanggan dalam sistem (L): {L:.2f}")
    st.write(f"Rata-rata waktu dalam sistem (W): {W:.2f} jam")
    st.write(f"Rata-rata waktu tunggu dalam antrean (Wq): {Wq:.2f} jam")

    fig3, ax3 = plt.subplots()
    categories = ["Dalam Sistem", "Dalam Antrean"]
    times = [W, Wq]
    ax3.bar(categories, times, color=["blue", "orange"])
    ax3.set_ylabel("Waktu (jam)")
    st.subheader("Visualisasi Waktu Tunggu")
    st.pyplot(fig3)
