import streamlit as st
import os

<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dijital Parazitoloji Kitabı & AI</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://unpkg.com/lucide@latest"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Inter', sans-serif; background-color: #f8fafc; }
        .glass { background: rgba(255, 255, 255, 0.95); backdrop-filter: blur(10px); }
        .custom-scroll::-webkit-scrollbar { width: 6px; }
        .custom-scroll::-webkit-scrollbar-track { background: #f1f1f1; }
        .custom-scroll::-webkit-scrollbar-thumb { background: #cbd5e1; border-radius: 10px; }
        .category-card:hover { transform: translateY(-3px); transition: all 0.3s ease; box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1); }
        .ai-bubble-bot { background: #f1f5f9; border-radius: 18px 18px 18px 0; border-left: 4px solid #8b5cf6; }
        .ai-bubble-user { background: #eff6ff; border-radius: 18px 18px 0 18px; border-right: 4px solid #3b82f6; }
        .animate-pop { animation: pop 0.3s ease-out; }
        @keyframes pop { from { opacity: 0; transform: scale(0.95); } to { opacity: 1; transform: scale(1); } }
        .basics-section h3 { @apply text-xl font-bold text-slate-900 mb-4 flex items-center gap-2; }
        .basics-section p { @apply text-slate-600 mb-6 leading-relaxed text-sm; }
        .basics-grid { @apply grid grid-cols-1 md:grid-cols-2 gap-6 mb-10; }
        .basics-card { @apply bg-white p-5 rounded-2xl border border-slate-200; }
    </style>
</head>
<body class="text-slate-800 h-screen flex flex-col overflow-hidden">

    <div id="app" class="flex h-full overflow-hidden">
        
        <!-- Sidebar Navigation -->
        <aside class="w-72 bg-slate-900 text-white flex-shrink-0 hidden md:flex flex-col border-r border-slate-800">
            <div class="p-6">
                <h1 class="text-xl font-bold flex items-center gap-2">
                    <i data-lucide="book-open" class="text-blue-400"></i>
                    Parazitoloji
                </h1>
                <p class="text-xs text-slate-400 mt-1 italic">Dijital Rehber & AI Asistan</p>
            </div>
            
            <nav class="flex-1 overflow-y-auto custom-scroll px-4 space-y-2 pb-6">
                <!-- Main Links -->
                <button onclick="changeView('home')" class="w-full flex items-center gap-3 px-3 py-2.5 rounded-xl hover:bg-slate-800 transition text-sm">
                    <i data-lucide="home" class="w-4 h-4"></i> Ana Sayfa
                </button>
                <button onclick="changeView('basics')" class="w-full flex items-center gap-3 px-3 py-2.5 rounded-xl bg-blue-600/10 text-blue-400 hover:bg-blue-600/20 transition text-sm font-semibold border border-blue-500/20">
                    <i data-lucide="info" class="w-4 h-4"></i> Temel Parazitoloji
                </button>

                <div class="pt-4 pb-2 text-[10px] font-bold text-slate-500 uppercase tracking-widest">I. PROTOZOA</div>
                <details class="group">
                    <summary class="flex items-center justify-between px-3 py-2 rounded-lg hover:bg-slate-800 cursor-pointer text-sm">
                        <span class="flex items-center gap-3"><i data-lucide="microscope" class="w-4 h-4 text-emerald-400"></i> Rhizopoda</span>
                        <i data-lucide="chevron-right" class="w-3 h-3 transition group-open:rotate-90"></i>
                    </summary>
                    <div class="pl-9 space-y-1 mt-1 text-xs text-slate-400">
                        <a href="#" onclick="filterBySub('Entamoeba')" class="block py-1.5 hover:text-white transition">Entamoeba Türleri</a>
                        <a href="#" onclick="filterBySub('Diğer Bağırsak Amipleri')" class="block py-1.5 hover:text-white transition">Bağırsak Amipleri</a>
                        <a href="#" onclick="filterBySub('Serbest Yaşayan')" class="block py-1.5 hover:text-white transition">Fırsatçı Amipler</a>
                    </div>
                </details>

                <details class="group">
                    <summary class="flex items-center justify-between px-3 py-2 rounded-lg hover:bg-slate-800 cursor-pointer text-sm">
                        <span class="flex items-center gap-3"><i data-lucide="zap" class="w-4 h-4 text-yellow-400"></i> Flagellata</span>
                        <i data-lucide="chevron-right" class="w-3 h-3 transition group-open:rotate-90"></i>
                    </summary>
                    <div class="pl-9 space-y-1 mt-1 text-xs text-slate-400">
                        <a href="#" onclick="filterBySub('Bağırsak Kamçılı')" class="block py-1.5 hover:text-white transition">Bağırsak & Ürogenital</a>
                        <a href="#" onclick="filterBySub('Kan ve Doku')" class="block py-1.5 hover:text-white transition">Kan ve Doku</a>
                    </div>
                </details>

                <button onclick="filterBySub('Ciliophora')" class="w-full flex items-center gap-3 px-3 py-2 rounded-lg hover:bg-slate-800 transition text-sm">
                    <i data-lucide="circle-slash" class="w-4 h-4 text-blue-400"></i> Ciliophora (Silliler)
                </button>

                <button onclick="filterBySub('Sporozoa')" class="w-full flex items-center gap-3 px-3 py-2 rounded-lg hover:bg-slate-800 transition text-sm">
                    <i data-lucide="target" class="w-4 h-4 text-red-400"></i> Sporozoa (Apicomplexa)
                </button>

                <div class="pt-4 pb-2 text-[10px] font-bold text-slate-500 uppercase tracking-widest">II. HELMİNTLER</div>
                <button onclick="filterBySub('Nematoda')" class="w-full flex items-center gap-3 px-3 py-2 rounded-lg hover:bg-slate-800 transition text-sm">
                    <i data-lucide="spline" class="w-4 h-4 text-orange-400"></i> Nematoda
                </button>
                <button onclick="filterBySub('Cestoda')" class="w-full flex items-center gap-3 px-3 py-2 rounded-lg hover:bg-slate-800 transition text-sm">
                    <i data-lucide="align-justify" class="w-4 h-4 text-pink-400"></i> Cestoda
                </button>
                <button onclick="filterBySub('Trematoda')" class="w-full flex items-center gap-3 px-3 py-2 rounded-lg hover:bg-slate-800 transition text-sm">
                    <i data-lucide="leaf" class="w-4 h-4 text-green-400"></i> Trematoda
                </button>

                <div class="pt-4 pb-2 text-[10px] font-bold text-slate-500 uppercase tracking-widest">III. ARTHROPODA</div>
                <button onclick="filterBySub('Arachnida')" class="w-full flex items-center gap-3 px-3 py-2 rounded-lg hover:bg-slate-800 transition text-sm">
                    <i data-lucide="bug" class="w-4 h-4 text-purple-400"></i> Arachnida
                </button>
                <button onclick="filterBySub('Insecta')" class="w-full flex items-center gap-3 px-3 py-2 rounded-lg hover:bg-slate-800 transition text-sm">
                    <i data-lucide="angry" class="w-4 h-4 text-amber-400"></i> Insecta
                </button>

                <div class="pt-6 mt-4 border-t border-slate-800 space-y-2">
                    <button onclick="changeView('aiTutor')" class="w-full flex items-center gap-3 px-3 py-2 rounded-xl bg-indigo-600/20 text-indigo-400 hover:bg-indigo-600/30 transition text-sm font-medium border border-indigo-500/30">
                        <i data-lucide="sparkles" class="w-4 h-4"></i> AI Soru Sor
                    </button>
                    <button onclick="toggleAdminMode()" id="adminBtn" class="w-full flex items-center gap-3 px-3 py-2 rounded-xl border border-slate-700 hover:bg-slate-800 transition text-xs">
                        <i data-lucide="settings" class="w-4 h-4"></i> Düzenleme Modu
                    </button>
                </div>
            </nav>
        </aside>

        <!-- Main Content Area -->
        <main class="flex-1 flex flex-col min-w-0 bg-slate-50 overflow-hidden">
            <header class="h-16 glass border-b border-slate-200 flex items-center justify-between px-6 sticky top-0 z-10">
                <div class="flex items-center flex-1 max-w-xl">
                    <div class="relative w-full">
                        <i data-lucide="search" class="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-slate-400"></i>
                        <input type="text" id="searchInput" oninput="handleSearch()" placeholder="Parazit veya temel kavram ara..." class="w-full bg-white/50 border border-slate-200 rounded-full py-2 pl-10 pr-4 text-sm focus:ring-2 focus:ring-blue-500 transition outline-none">
                    </div>
                </div>
                <div class="flex items-center gap-3 ml-4">
                    <button onclick="changeView('favorites')" class="p-2 text-slate-500 hover:text-pink-500 transition relative">
                        <i data-lucide="heart"></i>
                        <span id="favCount" class="absolute top-0 right-0 w-4 h-4 bg-pink-500 text-white text-[10px] rounded-full flex items-center justify-center">0</span>
                    </button>
                </div>
            </header>

            <div id="content" class="flex-1 overflow-y-auto p-6 custom-scroll">
                
                <!-- Home View -->
                <div id="homeView" class="animate-pop">
                    <div class="mb-10 text-center max-w-3xl mx-auto">
                        <h2 class="text-4xl font-extrabold text-slate-900 mb-4">Parazitoloji Atlası</h2>
                        <p class="text-slate-500 text-lg leading-relaxed">Tıbbi önemi olan parazitleri inceleyin, öğrenin ve kendi notlarınızı ekleyerek dijital kitabınızı oluşturun.</p>
                    </div>

                    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
                        <div onclick="changeView('basics')" class="bg-blue-600 p-6 rounded-3xl shadow-xl category-card cursor-pointer flex flex-col items-center text-center text-white">
                            <div class="w-16 h-16 bg-white/20 rounded-2xl flex items-center justify-center mb-4">
                                <i data-lucide="info" class="w-8 h-8"></i>
                            </div>
                            <h3 class="text-xl font-bold mb-1">Temel Bilgiler</h3>
                            <p class="text-sm text-blue-100">Giriş & Kavramlar</p>
                        </div>
                        <div onclick="filterByMain('Protozoa')" class="bg-white p-6 rounded-3xl shadow-sm border border-slate-200 category-card cursor-pointer flex flex-col items-center text-center">
                            <div class="w-16 h-16 bg-emerald-50 text-emerald-600 rounded-2xl flex items-center justify-center mb-4">
                                <i data-lucide="microscope" class="w-8 h-8"></i>
                            </div>
                            <h3 class="text-xl font-bold mb-1">Protozoa</h3>
                            <p class="text-sm text-slate-400">Tek hücreliler</p>
                        </div>
                        <div onclick="filterByMain('Helmintler')" class="bg-white p-6 rounded-3xl shadow-sm border border-slate-200 category-card cursor-pointer flex flex-col items-center text-center">
                            <div class="w-16 h-16 bg-orange-50 text-orange-600 rounded-2xl flex items-center justify-center mb-4">
                                <i data-lucide="layout-list" class="w-8 h-8"></i>
                            </div>
                            <h3 class="text-xl font-bold mb-1">Helmintler</h3>
                            <p class="text-sm text-slate-400">Solucanlar</p>
                        </div>
                        <div onclick="filterByMain('Artropodlar')" class="bg-white p-6 rounded-3xl shadow-sm border border-slate-200 category-card cursor-pointer flex flex-col items-center text-center">
                            <div class="w-16 h-16 bg-red-50 text-red-600 rounded-2xl flex items-center justify-center mb-4">
                                <i data-lucide="bug" class="w-8 h-8"></i>
                            </div>
                            <h3 class="text-xl font-bold mb-1">Artropodlar</h3>
                            <p class="text-sm text-slate-400">Eklem Bacaklılar</p>
                        </div>
                    </div>
                </div>

                <div id="basicsView" class="hidden animate-pop max-w-5xl mx-auto basics-section">
                    <div class="flex items-center gap-4 mb-8">
                        <div class="w-12 h-12 bg-blue-600 text-white rounded-2xl flex items-center justify-center">
                            <i data-lucide="book-open"></i>
                        </div>
                        <h2 class="text-3xl font-black text-slate-900">Temel Parazitolojiye Giriş</h2>
                    </div>

                    <div class="basics-grid">
                        <div class="basics-card">
                            <h3><i data-lucide="layers" class="text-blue-500"></i> Parazitlerin Sınıflandırılması</h3>
                            <p>Parazitler; hücre yapıları, morfolojileri ve yaşam döngülerine göre 3 ana gruba ayrılır: Protozoonlar (tek hücreli), Helmintler (çok hücreli/solucanlar) ve Artropodlar (eklem bacaklılar).</p>
                        </div>
                        <div class="basics-card">
                            <h3><i data-lucide="git-branch" class="text-emerald-500"></i> Parazit Türleri</h3>
                            <p><strong>Zorunlu:</strong> Yaşamı boyunca parazit kalmalı. <br><strong>Fakültatif:</strong> Serbest de yaşayabilir. <br><strong>Ektoparazit:</strong> Deri üstünde. <br><strong>Endoparazit:</strong> Vücut içinde.</p>
                        </div>
                    </div>

                    <div class="basics-card mb-10">
                        <h3><i data-lucide="users" class="text-purple-500"></i> Simbiyoz Yaşam Şekilleri</h3>
                        <div class="grid grid-cols-1 sm:grid-cols-3 gap-4 mt-4">
                            <div class="p-4 bg-slate-50 rounded-xl">
                                <span class="font-bold text-blue-600">Mutualizm</span>
                                <p class="text-xs mt-1">İki tarafın da fayda sağladığı yaşam (Arı ve çiçek gibi).</p>
                            </div>
                            <div class="p-4 bg-slate-50 rounded-xl">
                                <span class="font-bold text-emerald-600">Kommensalizm</span>
                                <p class="text-xs mt-1">Biri fayda görürken diğeri zarar veya fayda görmez.</p>
                            </div>
                            <div class="p-4 bg-slate-50 rounded-xl">
                                <span class="font-bold text-red-600">Parazitizm</span>
                                <p class="text-xs mt-1">Bir canlının diğerinin üzerinden geçinerek ona zarar vermesi.</p>
                            </div>
                        </div>
                    </div>

                    <div class="basics-grid">
                        <div class="basics-card">
                            <h3><i data-lucide="user-plus" class="text-orange-500"></i> Konak Türleri</h3>
                            <p><strong>Son Konak:</strong> Parazitin erişkin halini barındıran canlı. <br><strong>Ara Konak:</strong> Larva veya eşeysiz çoğalan formu barındıran canlı. <br><strong>Rezervuar:</strong> Paraziti doğada tutan hayvanlar.</p>
                        </div>
                        <div class="basics-card">
                            <h3><i data-lucide="share-2" class="text-red-500"></i> Vektör Türleri</h3>
                            <p><strong>Biyolojik Vektör:</strong> Parazit vektör içinde gelişir (Anofel/Sıtma). <br><strong>Mekanik Vektör:</strong> Sadece taşıyıcıdır (Karasinek/Kontaminasyon).</p>
                        </div>
                    </div>

                    <div class="basics-card mb-10">
                        <h3><i data-lucide="syringe" class="text-teal-500"></i> Bulaşma Yolları</h3>
                        <div class="flex flex-wrap gap-2">
                            <span class="px-3 py-1 bg-teal-50 text-teal-700 rounded-full text-xs font-bold">Fekal-Oral</span>
                            <span class="px-3 py-1 bg-teal-50 text-teal-700 rounded-full text-xs font-bold">Vektör Isırığı</span>
                            <span class="px-3 py-1 bg-teal-50 text-teal-700 rounded-full text-xs font-bold">Transplasental</span>
                            <span class="px-3 py-1 bg-teal-50 text-teal-700 rounded-full text-xs font-bold">Deri Penetrasyonu</span>
                            <span class="px-3 py-1 bg-teal-50 text-teal-700 rounded-full text-xs font-bold">Cinsel Yol</span>
                        </div>
                    </div>

                    <div class="basics-grid">
                        <div class="basics-card">
                            <h3><i data-lucide="microscope" class="text-indigo-500"></i> Tanı Yöntemleri</h3>
                            <p><strong>Direkt:</strong> Mikroskobik inceleme (kist, trofozoit, larva). <br><strong>İndirekt:</strong> Seroloji (ELISA, IFA), Kültür yöntemleri, PCR ve Moleküler analizler.</p>
                        </div>
                        <div class="basics-card">
                            <h3><i data-lucide="palette" class="text-pink-500"></i> Boyama Teknikleri</h3>
                            <p><strong>Lugol:</strong> Geçici boyama. <br><strong>Giemsa:</strong> Kan preparatları (Sıtma). <br><strong>Trikrom:</strong> Kalıcı dışkı boyama. <br><strong>Asit-Fast (ARB):</strong> Cryptosporidium vb. için.</p>
                        </div>
                    </div>
                </div>

                <!-- List View -->
                <div id="listView" class="hidden animate-pop">
                    <div class="flex items-center justify-between mb-8">
                        <div>
                            <h2 id="listTitle" class="text-3xl font-bold text-slate-900">Parazit Listesi</h2>
                            <p id="listDesc" class="text-slate-500 text-sm mt-1">Kategoriye ait tüm kayıtlar.</p>
                        </div>
                        <button onclick="openEditModal(null)" id="addNewBtn" class="hidden bg-blue-600 text-white px-5 py-2.5 rounded-xl text-sm font-bold flex items-center gap-2 hover:bg-blue-700 transition">
                            <i data-lucide="plus" class="w-4 h-4"></i> Yeni Ekle
                        </button>
                    </div>
                    <div id="parasiteGrid" class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-6"></div>
                </div>

                <!-- Detail View -->
                <div id="detailView" class="hidden animate-pop max-w-4xl mx-auto pb-20">
                    <button onclick="changeView('listView')" class="mb-6 flex items-center gap-2 text-slate-500 hover:text-slate-900 font-medium transition">
                        <i data-lucide="arrow-left" class="w-4 h-4"></i> Geri Dön
                    </button>
                    <div id="detailContent" class="bg-white rounded-3xl border border-slate-200 overflow-hidden shadow-xl"></div>
                </div>

                <!-- AI Tutor View -->
                <div id="aiTutorView" class="hidden h-full flex flex-col max-w-3xl mx-auto">
                    <div id="chatHistory" class="flex-1 overflow-y-auto p-6 space-y-4 bg-white rounded-2xl border border-slate-200 mb-4 custom-scroll">
                        <div class="ai-bubble-bot p-4 max-w-[85%] text-sm">
                            Merhaba! Ben parazitoloji asistanınızım. Mnemonicler, bulaş yolları veya vaka sorularınız için buradayım.
                        </div>
                    </div>
                    <div class="flex gap-2 p-1 bg-white border border-slate-200 rounded-2xl shadow-sm">
                        <input type="text" id="aiInput" onkeypress="if(event.key === 'Enter') sendToAI()" placeholder="Soru sorun..." class="flex-1 px-4 py-3 outline-none">
                        <button onclick="sendToAI()" class="bg-indigo-600 text-white p-3 rounded-xl hover:bg-indigo-700 transition"><i data-lucide="send" class="w-5 h-5"></i></button>
                    </div>
                </div>
            </div>
        </main>
    </div>

    <script>
        const INITIAL_PARASITES = [
            // I. PROTOZOA - Rhizopoda
            { id: 1, name: "Entamoeba histolytica", mainCat: "Protozoa", subCat: "Entamoeba", classification: "Patojen Amip", lifeCycle: "Kist ve trofozoit formları. Kalın bağırsakta (çekum) yerleşir.", transmission: "Fekal-oral, kistli su/gıdalar.", clinical: "Amipli dizanteri (kanlı ishal), karaciğer apsesi.", diagnosis: "Dışkıda trofozoit/kist, PCR, Seroloji.", treatment: "Metronidazol, Tinidazol.", prevention: "Hijyen, su arıtımı.", isPathogenic: true },
            { id: 2, name: "Entamoeba dispar", mainCat: "Protozoa", subCat: "Entamoeba", classification: "Zararsız", lifeCycle: "E. histolytica'ya morfolojik ikizdir.", transmission: "Fekal-oral.", clinical: "Asemptomatik.", diagnosis: "Sadece PCR ile ayrılır.", treatment: "Gerekmez.", prevention: "Hijyen.", isPathogenic: false },
            { id: 3, name: "Entamoeba moshkovskii", mainCat: "Protozoa", subCat: "Entamoeba", classification: "Zararsız", lifeCycle: "Morfolojik olarak E. histolytica'ya benzer.", transmission: "Fekal-oral.", clinical: "Genellikle non-patojen.", diagnosis: "PCR.", treatment: "Gerekmez.", prevention: "Hijyen.", isPathogenic: false },
            { id: 4, name: "Entamoeba coli", mainCat: "Protozoa", subCat: "Entamoeba", classification: "Zararsız", lifeCycle: "8 çekirdekli kist yapısı karakteristiktir.", transmission: "Fekal-oral.", clinical: "Patojen değildir.", diagnosis: "Dışkı bakısı.", treatment: "Gerekmez.", prevention: "Genel sanitasyon.", isPathogenic: false },
            { id: 5, name: "Entamoeba hartmanni", mainCat: "Protozoa", subCat: "Entamoeba", classification: "Küçük Amip (Zararsız)", lifeCycle: "Küçük kist/trofozoit (10 mikron altı).", transmission: "Fekal-oral.", clinical: "Hastalık yapmaz.", diagnosis: "Dışkı bakısı.", treatment: "Gerekmez.", prevention: "Hijyen.", isPathogenic: false },
            { id: 6, name: "Entamoeba gingivalis", mainCat: "Protozoa", subCat: "Entamoeba", classification: "Ağız Amibi", lifeCycle: "Kist formu yoktur, sadece trofozoit.", transmission: "Tükürük, ortak eşya.", clinical: "Gingivit ve piyorede artış.", diagnosis: "Diş eti kazıntısı.", treatment: "Oral hijyen.", prevention: "Diş bakımı.", isPathogenic: false },
            { id: 7, name: "Entamoeba polecki", mainCat: "Protozoa", subCat: "Entamoeba", classification: "Zoonotik (Domuz)", lifeCycle: "Tek çekirdekli kistleri vardır.", transmission: "Domuz/maymun teması.", clinical: "Hafif gastrointestinal şikayet.", diagnosis: "Dışkı muayenesi.", treatment: "Metronidazol.", prevention: "Hayvan hijyeni.", isPathogenic: false },
            { id: 8, name: "Iodamoeba bütschlii", mainCat: "Protozoa", subCat: "Diğer Bağırsak Amipleri", classification: "Zararsız", lifeCycle: "Lugol ile boyanan büyük glikojen vakuolü.", transmission: "Fekal-oral.", clinical: "Patojen değildir.", diagnosis: "Dışkı bakısı.", treatment: "Gerekmez.", prevention: "Hijyen.", isPathogenic: false },
            { id: 9, name: "Endolimax nana", mainCat: "Protozoa", subCat: "Diğer Bağırsak Amipleri", classification: "En Küçük Amip", lifeCycle: "Karışık enfeksiyonlarda sık görülür.", transmission: "Fekal-oral.", clinical: "Zararsızdır.", diagnosis: "Dışkı bakısı.", treatment: "Gerekmez.", prevention: "Hijyen.", isPathogenic: false },
            { id: 10, name: "Naegleria fowleri", mainCat: "Protozoa", subCat: "Serbest Yaşayan", classification: "Beyin Yiyen Amip", lifeCycle: "Kist, trofozoit ve kamçılı formlar.", transmission: "Burun yoluyla kontamine su kaçması.", clinical: "Primer Amibik Meningoensefalit (PAM). Hızlı ölümcül.", diagnosis: "BOS incelemesi.", treatment: "Amfoterisin B.", prevention: "Burun klipsi, klorlama.", isPathogenic: true },
            { id: 11, name: "Acanthamoeba türleri", mainCat: "Protozoa", subCat: "Serbest Yaşayan", classification: "Fırsatçı Patojen", lifeCycle: "Yıldız şeklinde kistleri karakteristiktir.", transmission: "Lens solüsyonu, deri yarası.", clinical: "Keratit (lens kullanıcıları), GAE.", diagnosis: "Kornea kazıntısı, Biyopsi.", treatment: "Klorheksidin.", prevention: "Lens hijyeni.", isPathogenic: true },
            { id: 12, name: "Balamuthia mandrillaris", mainCat: "Protozoa", subCat: "Serbest Yaşayan", classification: "Fırsatçı", lifeCycle: "Toprak ve toz.", transmission: "Solunum veya deri lezyonu.", clinical: "Granülomatöz Amibik Ensefalit (GAE).", diagnosis: "Doku histolojisi.", treatment: "Miltefosin.", prevention: "Bilinmiyor.", isPathogenic: true },
            { id: 13, name: "Sappinia pedata", mainCat: "Protozoa", subCat: "Serbest Yaşayan", classification: "Nadir Patojen", lifeCycle: "Çift çekirdekli trofozoitler.", transmission: "Çevresel temas.", clinical: "Amebik Ensefalit vakaları.", diagnosis: "Görüntüleme ve Biyopsi.", treatment: "Amfoterisin B.", prevention: "Kişisel korunma.", isPathogenic: true },

            // I. PROTOZOA - Flagellata
            { id: 14, name: "Giardia lamblia", mainCat: "Protozoa", subCat: "Bağırsak Kamçılı", classification: "Kamçılı", lifeCycle: "Armut biçimli trofozoit (iki çekirdekli).", transmission: "Fekal-oral, kontamine su.", clinical: "Steatore (yağlı ishal), emilim bozukluğu.", diagnosis: "Dışkıda kist/trofozoit, Entero-test.", treatment: "Metronidazol.", prevention: "Su filtrasyonu.", isPathogenic: true },
            { id: 15, name: "Trichomonas vaginalis", mainCat: "Protozoa", subCat: "Bağırsak Kamçılı", classification: "STD (Cinsel Yolla)", lifeCycle: "Kist formu yoktur. Sadece trofozoit.", transmission: "Cinsel temas.", clinical: "Vajinit, kötü kokulu akıntı, çilek serviks.", diagnosis: "Taze akıntı bakısı.", treatment: "Metronidazol (Eş tedavisi!).", prevention: "Korumalı ilişki.", isPathogenic: true },
            { id: 16, name: "Trichomonas hominis", mainCat: "Protozoa", subCat: "Bağırsak Kamçılı", classification: "Zararsız", lifeCycle: "Kalın bağırsakta yerleşir.", transmission: "Fekal-oral.", clinical: "Hastalık yapmaz.", diagnosis: "Dışkı bakısı.", treatment: "Gerekmez.", prevention: "Hijyen.", isPathogenic: false },
            { id: 17, name: "Chilomastix mesnili", mainCat: "Protozoa", subCat: "Bağırsak Kamçılı", classification: "Zararsız", lifeCycle: "Limon şeklinde karakteristik kistler.", transmission: "Fekal-oral.", clinical: "Non-patojen.", diagnosis: "Dışkı muayenesi.", treatment: "Gerekmez.", prevention: "Hijyen.", isPathogenic: false },
            { id: 18, name: "Leishmania tropica", mainCat: "Protozoa", subCat: "Kan ve Doku", classification: "Kutanöz Leishmaniasis", lifeCycle: "Tatarcık sineğinde çoğalır.", transmission: "Phlebotomus ısırığı.", clinical: "Şark Çıbanı (Kuru tip).", diagnosis: "Lezyon yaymasında amastigot.", treatment: "Antimon bileşikleri.", prevention: "Sinek kontrolü.", isPathogenic: true },
            { id: 19, name: "Leishmania infantum", mainCat: "Protozoa", subCat: "Kan ve Doku", classification: "Viseral Leishmaniasis", lifeCycle: "Akdeniz tipi.", transmission: "Tatarcık ısırığı.", clinical: "Kala-azar, hepatosplenomegali.", diagnosis: "Kemik iliği aspirasyonu.", treatment: "Amfoterisin B.", prevention: "Vektör kontrolü.", isPathogenic: true },
            { id: 20, name: "Leishmania donovani", mainCat: "Protozoa", subCat: "Kan ve Doku", classification: "Viseral Leishmaniasis", lifeCycle: "Asya ve Hindistan.", transmission: "Vektör ısırığı.", clinical: "Viseral tutulum.", diagnosis: "Seroloji.", treatment: "Antimon.", prevention: "Sinek kontrolü.", isPathogenic: true },
            { id: 21, name: "Leishmania major", mainCat: "Protozoa", subCat: "Kan ve Doku", classification: "Kutanöz Leishmaniasis", lifeCycle: "Kırsal tip (Islak çıban).", transmission: "Tatarcık ısırığı.", clinical: "Hızla iyileşmeyen deri yarası.", diagnosis: "Yayma.", treatment: "Kriyoterapi, İlaçlar.", prevention: "Kemirgen kontrolü.", isPathogenic: true },
            { id: 22, name: "Leishmania braziliensis", mainCat: "Protozoa", subCat: "Kan ve Doku", classification: "Mukokutanöz", lifeCycle: "G. Amerika.", transmission: "Sinek ısırığı.", clinical: "Ağız ve burun kıkırdak yıkımı.", diagnosis: "Biyopsi.", treatment: "Miltefosin.", prevention: "Kişisel korunma.", isPathogenic: true },
            { id: 23, name: "Trypanosoma brucei", mainCat: "Protozoa", subCat: "Kan ve Doku", classification: "Afrika Uyku Hastalığı", lifeCycle: "Çeçe sineği ile bulaşır.", transmission: "Glossina ısırığı.", clinical: "Kış uykusu benzeri tablo, koma.", diagnosis: "Kan/BOS yayması.", treatment: "Suramin, Melarsoprol.", prevention: "Vektör kontrolü.", isPathogenic: true },
            { id: 24, name: "Trypanosoma cruzi", mainCat: "Protozoa", subCat: "Kan ve Doku", classification: "Chagas Hastalığı", lifeCycle: "Tahtakurusu dışkısından bulaşır.", transmission: "Reduviid dışkısı deri teması.", clinical: "Kardiyomiyopati, Megaözofagus.", diagnosis: "Xenodiagnoz.", treatment: "Benznidazol.", prevention: "Ev ilaçlaması.", isPathogenic: true },

            // I. PROTOZOA - Ciliophora
            { id: 25, name: "Balantidium coli", mainCat: "Protozoa", subCat: "Ciliophora", classification: "Silli", lifeCycle: "En büyük insan protozoonudur. Domuz rezervuar.", transmission: "Fekal-oral.", clinical: "Balantidial dizanteri.", diagnosis: "Dışkıda silli trofozoit.", treatment: "Tetrasiklin.", prevention: "Domuz hijyeni.", isPathogenic: true },

            // I. PROTOZOA - Sporozoa
            { id: 26, name: "Plasmodium falciparum", mainCat: "Protozoa", subCat: "Sporozoa", classification: "Sıtma (Malign)", lifeCycle: "Anofel sineğinde eşeyli, insanda eşeysiz.", transmission: "Dişi Anofel ısırığı.", clinical: "En ağır sıtma, serebral sıtma, böbrek yetmezliği.", diagnosis: "Kalın damla (Muz şeklinde gametosit).", treatment: "Artemisinin.", prevention: "Cibinlik.", isPathogenic: true },
            { id: 27, name: "Plasmodium vivax", mainCat: "Protozoa", subCat: "Sporozoa", classification: "Sıtma", lifeCycle: "Hipnozoit (uyku) formu vardır.", transmission: "Anofel ısırığı.", clinical: "Benign tersiyan sıtma (48 saatlik ateş).", diagnosis: "Kan yayması.", treatment: "Klorokin + Primakin.", prevention: "Vektör kontrolü.", isPathogenic: true },
            { id: 28, name: "Plasmodium malariae", mainCat: "Protozoa", subCat: "Sporozoa", classification: "Sıtma", lifeCycle: "72 saatlik ateş döngüsü.", transmission: "Anofel ısırığı.", clinical: "Kuartan sıtma.", diagnosis: "Kan yayması (Kuşak formu).", treatment: "Klorokin.", prevention: "Korunma.", isPathogenic: true },
            { id: 29, name: "Plasmodium ovale", mainCat: "Protozoa", subCat: "Sporozoa", classification: "Sıtma", lifeCycle: "P. vivax'a benzer.", transmission: "Anofel ısırığı.", clinical: "Tersiyan sıtma.", diagnosis: "Kan yayması.", treatment: "Primakin.", prevention: "Korunma.", isPathogenic: true },
            { id: 30, name: "Plasmodium knowlesi", mainCat: "Protozoa", subCat: "Sporozoa", classification: "Zoonotik Sıtma", lifeCycle: "Maymun kaynaklı.", transmission: "Anofel ısırığı.", clinical: "Ağır ve hızlı ateş.", diagnosis: "PCR.", treatment: "Sıtma ilaçları.", prevention: "Ormanlık alan teması.", isPathogenic: true },
            { id: 31, name: "Toxoplasma gondii", mainCat: "Protozoa", subCat: "Sporozoa", classification: "Doku Sporozoonu", lifeCycle: "Kedi ana konak.", transmission: "Çiğ et, kedi dışkısı, konjenital.", clinical: "Lenfadenopati, gebelerde konjenital hasar.", diagnosis: "Seroloji (Sabine-Feldman).", treatment: "Pirimetamin.", prevention: "Pişmiş et, kedi kumu hijyeni.", isPathogenic: true },
            { id: 32, name: "Cryptosporidium hominis", mainCat: "Protozoa", subCat: "Sporozoa", classification: "Opportunistic", lifeCycle: "Ookistleri klora dirençlidir.", transmission: "Fekal-oral, havuz suları.", clinical: "AIDS hastalarında öldürücü ishal.", diagnosis: "ARB (Kinyoun) boyama.", treatment: "Nitazoksanid.", prevention: "Su filtrasyonu.", isPathogenic: true },
            { id: 33, name: "Cyclospora cayetanensis", mainCat: "Protozoa", subCat: "Sporozoa", classification: "Opportunistic", lifeCycle: "Meyve ve sebzelerden bulaşır.", transmission: "Kontamine gıda.", clinical: "Uzun süreli ishal.", diagnosis: "ARB boyama.", treatment: "TMP-SMX.", prevention: "Gıda hijyeni.", isPathogenic: true },
            { id: 34, name: "Cystoisospora belli", mainCat: "Protozoa", subCat: "Sporozoa", classification: "Opportunistic", lifeCycle: "İnce bağırsakta yerleşir.", transmission: "Fekal-oral.", clinical: "Kolit, ishal.", diagnosis: "Dışkıda elipsoid ookist.", treatment: "TMP-SMX.", prevention: "Hijyen.", isPathogenic: true },
            { id: 35, name: "Babesia microti", mainCat: "Protozoa", subCat: "Sporozoa", classification: "Kan Paraziti", lifeCycle: "Kene ile bulaşır.", transmission: "Ixodes ısırığı.", clinical: "Malta haçı görünümü, hemoliz.", diagnosis: "Kan yayması.", treatment: "Azitromisin.", prevention: "Kene kontrolü.", isPathogenic: true },

            // II. HELMİNTLER - Nematoda
            { id: 36, name: "Ascaris lumbricoides", mainCat: "Helmintler", subCat: "Nematoda", classification: "Dev Yuvarlak Solucan", lifeCycle: "Bağırsak -> Karaciğer -> Akciğer -> Bağırsak.", transmission: "Toprakla bulaşmış gıda.", clinical: "Löffler Sendromu (öksürük), bağırsak tıkanıklığı.", diagnosis: "Dışkıda yumurta.", treatment: "Albendazol.", prevention: "Sanitasyon.", isPathogenic: true },
            { id: 37, name: "Enterobius vermicularis", mainCat: "Helmintler", subCat: "Nematoda", classification: "Kıl Kurdu", lifeCycle: "Gece perianal bölgeye yumurtlama.", transmission: "Kontamine eller, fekal-oral.", clinical: "Şiddetli gece kaşıntısı, uykusuzluk.", diagnosis: "Seloteyp testi.", treatment: "Pirantel Pamoat.", prevention: "Kişisel temizlik.", isPathogenic: true },
            { id: 38, name: "Trichuris trichiura", mainCat: "Helmintler", subCat: "Nematoda", classification: "Kamçılı Solucan", lifeCycle: "Kalın bağırsak (çekum).", transmission: "Fekal-oral.", clinical: "Rektal prolapsus.", diagnosis: "Limon şeklinde yumurtalar.", treatment: "Mebendazol.", prevention: "Hijyen.", isPathogenic: true },
            { id: 39, name: "Strongyloides stercoralis", mainCat: "Helmintler", subCat: "Nematoda", classification: "İplik Kurdu", lifeCycle: "Otienfeksiyon yapabilir.", transmission: "Deriden larva girişi.", clinical: "Larva currens, ishal.", diagnosis: "Dışkıda rhabditiform larva.", treatment: "İvermektin.", prevention: "Ayakkabı giyme.", isPathogenic: true },
            { id: 40, name: "Ancylostoma duodenale", mainCat: "Helmintler", subCat: "Nematoda", classification: "Kancalı Kurt", lifeCycle: "Kan emerek anemı yapar.", transmission: "Deri yoluyla.", clinical: "Demir eksikliği anemisi.", diagnosis: "Dışkıda yumurta.", treatment: "Albendazol.", prevention: "Sanitasyon.", isPathogenic: true },
            { id: 41, name: "Necator americanus", mainCat: "Helmintler", subCat: "Nematoda", classification: "Yeni Dünya Kancalı Kurdu", lifeCycle: "Ancylostoma'ya benzer.", transmission: "Deri.", clinical: "Anemi.", diagnosis: "Dışkı bakısı.", treatment: "Mebendazol.", prevention: "Ayakkabı.", isPathogenic: true },
            { id: 42, name: "Trichinella spiralis", mainCat: "Helmintler", subCat: "Nematoda", classification: "Kas Kurdu", lifeCycle: "Kaslarda kistleşme.", transmission: "Çiğ domuz/vahşi hayvan eti.", clinical: "Kas ağrısı, periorbital ödem.", diagnosis: "Kas biyopsisi, Seroloji.", treatment: "Albendazol + Steroid.", prevention: "Pişmiş et.", isPathogenic: true },
            { id: 43, name: "Wuchereria bancrofti", mainCat: "Helmintler", subCat: "Nematoda", classification: "Fil Hastalığı", lifeCycle: "Sivrisinek vektörü.", transmission: "Isırık.", clinical: "Elefantiyazis.", diagnosis: "Gece alınan kanda mikrofilaria.", treatment: "DEC.", prevention: "Sinek kontrolü.", isPathogenic: true },
            { id: 44, name: "Brugia malayi", mainCat: "Helmintler", subCat: "Nematoda", classification: "Fil Hastalığı", lifeCycle: "Asya tipi.", transmission: "Sivrisinek.", clinical: "Ödem, lenfanjit.", diagnosis: "Kan yayması.", treatment: "DEC.", prevention: "Vektör kontrolü.", isPathogenic: true },
            { id: 45, name: "Loa loa", mainCat: "Helmintler", subCat: "Nematoda", classification: "Göz Kurdu", lifeCycle: "Chrysops sineği.", transmission: "Sinek ısırığı.", clinical: "Calabar şişliği, gözde kurt.", diagnosis: "Gözlem.", treatment: "Cerrahi çıkarma.", prevention: "Sinek kontrolü.", isPathogenic: true },
            { id: 46, name: "Onchocerca volvulus", mainCat: "Helmintler", subCat: "Nematoda", classification: "Nehir Körlüğü", lifeCycle: "Kara sinek vektörü.", transmission: "Simulium ısırığı.", clinical: "Körlük, deri nodülleri.", diagnosis: "Deri kazıntısı (Skin snip).", treatment: "İvermektin.", prevention: "Vektör kontrolü.", isPathogenic: true },
            { id: 47, name: "Dracunculus medinensis", mainCat: "Helmintler", subCat: "Nematoda", classification: "Medine Kurdu", lifeCycle: "Su piresi ara konak.", transmission: "Filtrelenmemiş su.", clinical: "Deri ülseri.", diagnosis: "Gözle görülür kurt.", treatment: "Sararak çıkarma.", prevention: "Su filtrasyonu.", isPathogenic: true },
            { id: 48, name: "Toxocara canis / cati", mainCat: "Helmintler", subCat: "Nematoda", classification: "Larva Migrans", lifeCycle: "Kedi/köpek dışkısı.", transmission: "Toprak/kum teması.", clinical: "Viseral ve Oküler Larva Migrans.", diagnosis: "ELISA.", treatment: "Albendazol.", prevention: "Hayvan bakımı.", isPathogenic: true },

            // II. HELMİNTLER - Cestoda
            { id: 49, name: "Taenia saginata", mainCat: "Helmintler", subCat: "Cestoda", classification: "Sığır Şeriti", lifeCycle: "Ara konak sığır.", transmission: "Çiğ sığır eti.", clinical: "Karın ağrısı, halka dökülmesi.", diagnosis: "Halkaların görülmesi.", treatment: "Prazikuantel.", prevention: "Kontrollü et.", isPathogenic: true },
            { id: 50, name: "Taenia solium", mainCat: "Helmintler", subCat: "Cestoda", classification: "Domuz Şeriti", lifeCycle: "Sistiserkoz yapabilir.", transmission: "Yumurta alımı veya et.", clinical: "Nörosistiserkoz (beyin kisti).", diagnosis: "Görüntüleme.", treatment: "Prazikuantel.", prevention: "Hijyen.", isPathogenic: true },
            { id: 51, name: "Hymenolepis nana", mainCat: "Helmintler", subCat: "Cestoda", classification: "Cüce Şerit", lifeCycle: "Direkt döngü.", transmission: "Fekal-oral.", clinical: "İshal, iştahsızlık.", diagnosis: "Dışkıda yumurta.", treatment: "Prazikuantel.", prevention: "Kişisel temizlik.", isPathogenic: true },
            { id: 52, name: "Hymenolepis diminuta", mainCat: "Helmintler", subCat: "Cestoda", classification: "Fare Şeriti", lifeCycle: "Ara konak böcekler.", transmission: "Böcekli gıda.", clinical: "Hafif seyirli.", diagnosis: "Dışkı bakısı.", treatment: "Prazikuantel.", prevention: "Kemirgen kontrolü.", isPathogenic: true },
            { id: 53, name: "Echinococcus granulosus", mainCat: "Helmintler", subCat: "Cestoda", classification: "Kist Hidatik", lifeCycle: "Köpek dışkısından yumurta.", transmission: "Kirli eller/sebze.", clinical: "KC ve Akciğerde kistler.", diagnosis: "Seroloji, USG.", treatment: "Albendazol, PAIR.", prevention: "Köpek aşılaması.", isPathogenic: true },
            { id: 54, name: "Echinococcus multilocularis", mainCat: "Helmintler", subCat: "Cestoda", classification: "Alveoler Kist", lifeCycle: "Tilki kaynaklı.", transmission: "Doğa teması.", clinical: "Tümör benzeri yayılım.", diagnosis: "Seroloji.", treatment: "Cerrahi.", prevention: "Yabani hayvan teması.", isPathogenic: true },
            { id: 55, name: "Diphyllobothrium latum", mainCat: "Helmintler", subCat: "Cestoda", classification: "Balık Şeriti", lifeCycle: "Tatlı su balığı.", transmission: "Çiğ balık.", clinical: "B12 vitamini eksikliği anemisi.", diagnosis: "Yumurta tespiti.", treatment: "Prazikuantel.", prevention: "Pişmiş balık.", isPathogenic: true },
            { id: 56, name: "Dipylidium caninum", mainCat: "Helmintler", subCat: "Cestoda", classification: "Köpek Şeriti", lifeCycle: "Pire ara konaktır.", transmission: "Yanlışlıkla pire yutma.", clinical: "Halka dökülmesi.", diagnosis: "Gözlem.", treatment: "Prazikuantel.", prevention: "Pire kontrolü.", isPathogenic: true },

            // II. HELMİNTLER - Trematoda
            { id: 57, name: "Fasciola hepatica", mainCat: "Helmintler", subCat: "Trematoda", classification: "KC Kelebeği", lifeCycle: "Salyangoz ara konaktır.", transmission: "Metaserkaryalı su bitkileri.", clinical: "Safra yolu tıkanıklığı, ateş.", diagnosis: "Yumurta bakısı.", treatment: "Trikla-bendazol.", prevention: "Bitki temizliği.", isPathogenic: true },
            { id: 58, name: "Fasciola gigantica", mainCat: "Helmintler", subCat: "Trematoda", classification: "Dev Kelebek", lifeCycle: "F. hepatica'ya benzer.", transmission: "Su bitkileri.", clinical: "KC hasarı.", diagnosis: "Dışkı.", treatment: "İlaçlar.", prevention: "Hijyen.", isPathogenic: true },
            { id: 59, name: "Dicrocoelium dendriticum", mainCat: "Helmintler", subCat: "Trematoda", classification: "Küçük Kelebek", lifeCycle: "Salyangoz ve karınca.", transmission: "Karınca yutma.", clinical: "Safra yolu irritasyonu.", diagnosis: "Yumurta.", treatment: "Prazikuantel.", prevention: "Mera kontrolü.", isPathogenic: true },
            { id: 60, name: "Schistosoma haematobium", mainCat: "Helmintler", subCat: "Trematoda", classification: "Ürogenital", lifeCycle: "Tatlı su salyangozu.", transmission: "Suyla temas.", clinical: "Hematüri, mesane kanseri riski.", diagnosis: "İdrarda yumurta.", treatment: "Prazikuantel.", prevention: "Kirli sudan kaçınma.", isPathogenic: true },
            { id: 61, name: "Schistosoma mansoni", mainCat: "Helmintler", subCat: "Trematoda", classification: "Bağırsak", lifeCycle: "Bağırsak venleri.", transmission: "Deri yoluyla.", clinical: "Siroz, portal tansiyon.", diagnosis: "Dışkıda yumurta.", treatment: "Prazikuantel.", prevention: "Hijyen.", isPathogenic: true },
            { id: 62, name: "Schistosoma japonicum", mainCat: "Helmintler", subCat: "Trematoda", classification: "Doğu Şistozom", lifeCycle: "Mezenterik venler.", transmission: "Deri.", clinical: "Karaciğer hasarı.", diagnosis: "Dışkı.", treatment: "Prazikuantel.", prevention: "Kontrol.", isPathogenic: true },
            { id: 63, name: "Opisthorchis sinensis (Clonorchis)", mainCat: "Helmintler", subCat: "Trematoda", classification: "Çin KC Kelebeği", lifeCycle: "Balık ara konak.", transmission: "Çiğ balık.", clinical: "Safra yolu kanseri riski.", diagnosis: "Yumurta.", treatment: "Prazikuantel.", prevention: "Pişmiş balık.", isPathogenic: true },
            { id: 64, name: "Paragonimus westermani", mainCat: "Helmintler", subCat: "Trematoda", classification: "Akciğer Kelebeği", lifeCycle: "Yengeç/istakoz.", transmission: "Çiğ deniz ürünü.", clinical: "Kanlı balgam.", diagnosis: "Balgamda yumurta.", treatment: "Prazikuantel.", prevention: "Pişmiş kabuklu.", isPathogenic: true },

            // III. ARTHROPODA - Arachnida
            { id: 65, name: "Sarcoptes scabiei", mainCat: "Artropodlar", subCat: "Arachnida", classification: "Uyuz", lifeCycle: "Deri altı tüneller.", transmission: "Yakın temas.", clinical: "Gece artan kaşıntı.", diagnosis: "Deri kazıntısı.", treatment: "Permetrin.", prevention: "Eşya hijyeni.", isPathogenic: true },
            { id: 66, name: "Demodex folliculorum", mainCat: "Artropodlar", subCat: "Arachnida", classification: "Kirpik Akarı", lifeCycle: "Kıl dipleri.", transmission: "Temas.", clinical: "Blefarit, akne tetikleyici.", diagnosis: "Kıl örneği.", treatment: "Çay ağacı yağı.", prevention: "Yüz hijyeni.", isPathogenic: true },
            { id: 67, name: "Ixodes türleri", mainCat: "Artropodlar", subCat: "Arachnida", classification: "Sert Kene", lifeCycle: "Vektör.", transmission: "Isırık.", clinical: "Lyme Hastalığı iletimi.", diagnosis: "Gözlem.", treatment: "Kene çıkarma.", prevention: "Kovucu.", isPathogenic: true },
            { id: 68, name: "Hyalomma türleri", mainCat: "Artropodlar", subCat: "Arachnida", classification: "Sert Kene", lifeCycle: "Vektör.", transmission: "Isırık.", clinical: "KKKA (Kırım Kongo) iletimi.", diagnosis: "Öykü.", treatment: "Destek.", prevention: "Korunma.", isPathogenic: true },
            { id: 69, name: "Dermacentor türleri", mainCat: "Artropodlar", subCat: "Arachnida", classification: "Kene", lifeCycle: "Vektör.", transmission: "Isırık.", clinical: "Kayalık Dağlar Ateşi.", diagnosis: "Klinik.", treatment: "Antibiyotik.", prevention: "Kontrol.", isPathogenic: true },
            { id: 70, name: "Argas türleri", mainCat: "Artropodlar", subCat: "Arachnida", classification: "Yumuşak Kene", lifeCycle: "Kümes kaynaklı.", transmission: "Gece ısırığı.", clinical: "Toksik tablo.", diagnosis: "Öykü.", treatment: "Semptomatik.", prevention: "İlaçlama.", isPathogenic: true },

            // III. ARTHROPODA - Insecta
            { id: 71, name: "Pediculus humanus", mainCat: "Artropodlar", subCat: "Insecta", classification: "Bit", lifeCycle: "Sirke (yumurta).", transmission: "Direkt temas.", clinical: "Baş kaşıntısı.", diagnosis: "Gözlem.", treatment: "Permetrin.", prevention: "Taramak.", isPathogenic: true },
            { id: 72, name: "Pthirus pubis", mainCat: "Artropodlar", subCat: "Insecta", classification: "Kasık Biti", lifeCycle: "Yengeç bit.", transmission: "Cinsel temas.", clinical: "Mavi lekeler.", diagnosis: "Bit tespiti.", treatment: "İlaç.", prevention: "Hijyen.", isPathogenic: true },
            { id: 73, name: "Pulex irritans", mainCat: "Artropodlar", subCat: "Insecta", classification: "Pire", lifeCycle: "İnsan piresi.", transmission: "Isırık.", clinical: "Papüller.", diagnosis: "Isırık izi.", treatment: "Krem.", prevention: "İlaçlama.", isPathogenic: true },
            { id: 74, name: "Ctenocephalides canis", mainCat: "Artropodlar", subCat: "Insecta", classification: "Hayvan Piresi", lifeCycle: "Zoonotik.", transmission: "Isırık.", clinical: "Kaşıntı.", diagnosis: "Gözlem.", treatment: "İlaç.", prevention: "Evcil hayvan bakımı.", isPathogenic: true },
            { id: 75, name: "Xenopsylla cheopis", mainCat: "Artropodlar", subCat: "Insecta", classification: "Sıçan Piresi", lifeCycle: "Veba vektörü.", transmission: "Isırık.", clinical: "Veba iletimi.", diagnosis: "Anamnez.", treatment: "Antibiyotik.", prevention: "Fare kontrolü.", isPathogenic: true },
            { id: 76, name: "Cimex lectularius", mainCat: "Artropodlar", subCat: "Insecta", classification: "Tahtakurusu", lifeCycle: "Gece beslenir.", transmission: "Isırık.", clinical: "Doğrusal döküntü.", diagnosis: "Yatak kontrolü.", treatment: "İlaçlama.", prevention: "Hijyen.", isPathogenic: true },
            { id: 77, name: "Anopheles, Culex, Aedes", mainCat: "Artropodlar", subCat: "Insecta", classification: "Sivrisinekler", lifeCycle: "Vektör.", transmission: "Isırık.", clinical: "Sıtma, Dang, Zika iletimi.", diagnosis: "Klinik.", treatment: "Vektör savaşı.", prevention: "Aşı, kovucu.", isPathogenic: true },
            { id: 78, name: "Phlebotomus türleri", mainCat: "Artropodlar", subCat: "Insecta", classification: "Tatarcık", lifeCycle: "Vektör.", transmission: "Isırık.", clinical: "Leishmaniasis iletimi.", diagnosis: "Klinik.", treatment: "Korunma.", prevention: "Tel örgü.", isPathogenic: true },
            { id: 79, name: "Glossina türleri", mainCat: "Artropodlar", subCat: "Insecta", classification: "Çeçe Sineği", lifeCycle: "Vektör.", transmission: "Isırık.", clinical: "Uyku hastalığı iletimi.", diagnosis: "Öykü.", treatment: "Sinek kontrolü.", prevention: "Özel tuzak.", isPathogenic: true },
            { id: 80, name: "Lucilia sericata", mainCat: "Artropodlar", subCat: "Insecta", classification: "Miyaz", lifeCycle: "Yara miyazı.", transmission: "Sinek yumurtası.", clinical: "Yarada larvalar.", diagnosis: "Gözlem.", treatment: "Cerrahi.", prevention: "Yara bakımı.", isPathogenic: true },
            { id: 81, name: "Dermatobia hominis", mainCat: "Artropodlar", subCat: "Insecta", classification: "Miyaz", lifeCycle: "Deri miyazı.", transmission: "Isırıkla bulaş.", clinical: "Deri altı kurt.", diagnosis: "Fizik muayene.", treatment: "Çıkarma.", prevention: "Kovucu.", isPathogenic: true },
            { id: 82, name: "Wohlfahrtia magnifica", mainCat: "Artropodlar", subCat: "Insecta", classification: "Miyaz", lifeCycle: "Vücut boşlukları.", transmission: "Larva bırakma.", clinical: "Dokuda harabiyet.", diagnosis: "Gözlem.", treatment: "Temizlik.", prevention: "Sinek kontrolü.", isPathogenic: true }
        ];

        let parasites = JSON.parse(localStorage.getItem('parasites')) || INITIAL_PARASITES;
        let currentView = 'home';
        let favorites = JSON.parse(localStorage.getItem('favorites')) || [];
        let isAdminMode = false;

        function init() {
            renderFavoritesCount();
            lucide.createIcons();
            changeView('home');
        }

        function changeView(view) {
            const views = ['homeView', 'listView', 'detailView', 'aiTutorView', 'basicsView'];
            views.forEach(v => {
                const el = document.getElementById(v);
                if (el) el.classList.add('hidden');
            });
            
            document.getElementById(view + 'View').classList.remove('hidden');
            currentView = view;
            window.scrollTo(0,0);
            lucide.createIcons();
        }

        function filterBySub(sub) {
            const filtered = parasites.filter(p => p.subCat.toLowerCase().includes(sub.toLowerCase()) || p.mainCat.toLowerCase().includes(sub.toLowerCase()));
            document.getElementById('listTitle').innerText = sub;
            document.getElementById('listDesc').innerText = `${sub} grubuna ait kayıtlar.`;
            changeView('list');
            renderList(filtered);
        }

        function filterByMain(main) {
            const filtered = parasites.filter(p => p.mainCat === main);
            document.getElementById('listTitle').innerText = main;
            document.getElementById('listDesc').innerText = `${main} kategorisindeki tüm parazitler.`;
            changeView('list');
            renderList(filtered);
        }

        function handleSearch() {
            const q = document.getElementById('searchInput').value.toLowerCase();
            if (q.length < 2) return;
            const filtered = parasites.filter(p => 
                p.name.toLowerCase().includes(q) || 
                p.clinical.toLowerCase().includes(q) ||
                p.subCat.toLowerCase().includes(q)
            );
            document.getElementById('listTitle').innerText = `"${q}" İçin Sonuçlar`;
            changeView('list');
            renderList(filtered);
        }

        function renderList(data) {
            const grid = document.getElementById('parasiteGrid');
            grid.innerHTML = '';
            
            data.forEach(p => {
                const isFav = favorites.includes(p.id);
                const card = document.createElement('div');
                card.className = "bg-white p-6 rounded-3xl border border-slate-200 shadow-sm category-card cursor-pointer group flex flex-col";
                card.onclick = (e) => {
                    if (e.target.closest('.fav-btn')) return;
                    renderDetail(p.id);
                };
                
                card.innerHTML = `
                    <div class="flex justify-between items-start mb-4">
                        <span class="px-3 py-1 bg-slate-100 text-slate-500 text-[10px] font-bold rounded-full uppercase">${p.subCat}</span>
                        <button onclick="toggleFavorite(${p.id})" class="fav-btn p-2 rounded-full hover:bg-pink-50 transition ${isFav ? 'text-pink-500' : 'text-slate-300'}">
                            <i data-lucide="heart" class="w-5 h-5 ${isFav ? 'fill-current' : ''}"></i>
                        </button>
                    </div>
                    <h3 class="text-xl font-bold text-slate-800 mb-2 group-hover:text-blue-600 transition">${p.name}</h3>
                    <p class="text-sm text-slate-500 line-clamp-2 mb-4">${p.clinical}</p>
                    <div class="mt-auto pt-4 border-t border-slate-50 flex justify-between items-center">
                        <span class="text-xs font-medium text-blue-500">Detayları Gör</span>
                    </div>
                `;
                grid.appendChild(card);
            });
            lucide.createIcons();
        }

        function renderDetail(id) {
            const p = parasites.find(item => item.id === id);
            if (!p) return;
            
            const container = document.getElementById('detailContent');
            changeView('detail');
            
            container.innerHTML = `
                <div class="bg-gradient-to-r from-slate-900 to-slate-800 p-10 text-white">
                    <span class="px-3 py-1 bg-white/10 text-white/70 text-[10px] font-bold rounded-full uppercase tracking-widest mb-3 inline-block">${p.subCat}</span>
                    <h2 class="text-4xl font-black mb-2">${p.name}</h2>
                    <p class="text-blue-300 font-medium italic">${p.classification}</p>
                </div>
                <div class="p-10 grid grid-cols-1 md:grid-cols-2 gap-10">
                    <div class="space-y-8">
                        <div>
                            <h4 class="flex items-center gap-2 text-sm font-bold text-slate-900 uppercase tracking-wider mb-3"><i data-lucide="repeat" class="w-4 h-4 text-blue-500"></i> Yaşam Döngüsü</h4>
                            <p class="text-slate-600 text-sm leading-relaxed">${p.lifeCycle}</p>
                        </div>
                        <div>
                            <h4 class="flex items-center gap-2 text-sm font-bold text-slate-900 uppercase tracking-wider mb-3"><i data-lucide="truck" class="w-4 h-4 text-emerald-500"></i> Bulaş Yolu</h4>
                            <p class="text-slate-600 text-sm leading-relaxed">${p.transmission}</p>
                        </div>
                        <div>
                            <h4 class="flex items-center gap-2 text-sm font-bold text-slate-900 uppercase tracking-wider mb-3"><i data-lucide="activity" class="w-4 h-4 text-red-500"></i> Klinik Bulgular</h4>
                            <p class="text-slate-600 text-sm leading-relaxed">${p.clinical}</p>
                        </div>
                    </div>
                    <div class="space-y-8">
                        <div>
                            <h4 class="flex items-center gap-2 text-sm font-bold text-slate-900 uppercase tracking-wider mb-3"><i data-lucide="search" class="w-4 h-4 text-purple-500"></i> Tanı</h4>
                            <p class="text-slate-600 text-sm leading-relaxed">${p.diagnosis}</p>
                        </div>
                        <div>
                            <h4 class="flex items-center gap-2 text-sm font-bold text-slate-900 uppercase tracking-wider mb-3"><i data-lucide="pill" class="w-4 h-4 text-amber-500"></i> Tedavi</h4>
                            <p class="bg-amber-50 text-amber-900 p-4 rounded-2xl text-sm border border-amber-100">${p.treatment}</p>
                        </div>
                    </div>
                </div>
            `;
            lucide.createIcons();
        }

        function toggleFavorite(id) {
            if (favorites.includes(id)) {
                favorites = favorites.filter(fid => fid !== id);
            } else {
                favorites.push(id);
            }
            localStorage.setItem('favorites', JSON.stringify(favorites));
            renderFavoritesCount();
            if (currentView === 'list') renderList(parasites);
        }

        function renderFavoritesCount() {
            document.getElementById('favCount').innerText = favorites.length;
        }

        function sendToAI() {
            const input = document.getElementById('aiInput');
            const text = input.value.trim();
            if (!text) return;
            
            const history = document.getElementById('chatHistory');
            const userBubble = document.createElement('div');
            userBubble.className = "ai-bubble-user p-4 max-w-[85%] text-sm ml-auto";
            userBubble.innerText = text;
            history.appendChild(userBubble);
            input.value = '';
            
            setTimeout(() => {
                const botBubble = document.createElement('div');
                botBubble.className = "ai-bubble-bot p-4 max-w-[85%] text-sm";
                botBubble.innerHTML = `<strong>Analiz:</strong> ${text} konusu için kitabın "Temel Bilgiler" kısmındaki laboratuvar tanı yöntemlerini inceleyebilirsiniz. Spesifik olarak hangi parazitin yaşam döngüsünü mnemonic ile açıklayayım?`;
                history.appendChild(botBubble);
                history.scrollTop = history.scrollHeight;
            }, 800);
        }

        window.onload = init;
    </script>
</body>
</html>
st.markdown("---")
st.caption("© 2026 Kırşehir Ahi Evran Üniversitesi Tıp Fakültesi - Tıbbi Parazitoloji Anabilim Dalı")
