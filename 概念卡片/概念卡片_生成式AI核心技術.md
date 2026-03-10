---
aliases:
  - 生成式AI技術
  - VAE
  - GAN
  - Transformer
  - Diffusion Model
tags:
  - 概念卡片
  - 生成式AI
Up: "[[科目二：生成式 AI 應用與規劃]]"
Related: 
---

# ⚙️ 概念卡片_生成式AI核心技術

## 📝 介紹與詳細說明

### 🟢 初學者/非技術視角 (跨部門溝通)
現在最紅的 AI 不只能幫你「分類」和「預測」，甚至能憑空「生出」原本不存在的文章、圖片與音樂。背後主要有三位大功臣：
1. **Transformer (語言天才)**：它是所有 ChatGPT 等聊天機器人的大腦。以前的 AI 看文章是一口一口慢慢吃，容易忘記前面；但 Transformer 能「一眼看完全局」，馬上抓住重點和前後文的關係，所以講話非常有邏輯。
2. **GAN (造假雙神)**：由「造假大師」和「鑑定專家」組成的雙人組。造假者拼命畫出假畫，鑑定專家拼命抓漏。經過幾萬回合的較量後，造假者就能畫出連專家都分不出來的超級逼真人臉 (例如 Deepfake 換臉技術)。
3. **Diffusion (除雜訊畫師)**：這是現在最頂級的「畫家」(像是 Midjourney)。它的畫畫方式很特別，是先在腦海裡撒一把沙子（一堆雜訊），然後慢慢把沙子撥開、雕琢出細節，最後變成一張極其精美的高解析度照片。

### 🔵 深度專業視角 (核心技術與底層邏輯)
生成式 AI 突破了判別模型 (Discriminative Model) 僅能劃分決策邊界 $P(Y|X)$ 的限制，轉而學習資料的真實分佈機率 $P(X)$ 以進行採樣生成。經典基礎架構如下：
1. **VAE (Variational Autoencoder)**：
   - 透過 Encoder 將輸入映射為潛在空間 (Latent Space) 的高斯分佈參數 (均值與變異數)，再從中採樣交由 Decoder 還原。優點是潛在空間平滑可插值，缺點是生成樣本常有模糊 (Blurry) 現象。
2. **GAN (Generative Adversarial Network)**：
   - 利用 Min-Max 賽局原理。Generator $G$ 從隨機噪音中生成數據，Discriminator $D$ 判斷真偽。優點是生成的圖像極為銳利逼真，缺點是訓練極不穩定，極易發生模式崩潰 (Mode Collapse)。
3. **Transformer**：
   - 徹底捨棄了傳統 RNN/CNN，完全依賴自注意力機制 (Self-Attention)。具備高度的平行運算能力與無限制長度的全局感受野，是現代大型語言模型 (LLM) 的絕對基底。
4. **Diffusion Model (擴散模型)**：
   - 包含前向加噪 (Forward Diffusion) 與反向去噪 (Reverse Denoising) 兩個馬可夫鏈過程。模型透過 U-Net 學習在每個時間步預測微小雜訊並將其減去。現已全面超越 GAN，成為圖像生成領域 (如 Stable Diffusion) 的 SOTA (State-of-the-Art)。

---

## 🚀 進階延伸研究 (Deep Dive)
除了了解生成式 AI 的大分類，要真正將大型語言模型落地在企業應用中，還需要仰賴許多外掛與微調技術來克服模型的限制。核心技術發展已整理為專文：

- 🔗 **LLM 落地三大神器**：請參閱 [[專題探討_Transformer與RAG-LoRA微調技術]] (涵蓋自注意力機制、檢索外掛大腦與低階調適微調)

---

## 🎯 常見測驗題型

## 🎯 常見測驗題型

> [!question] 選擇題 1：
> OpenAI 所發表並震驚全球的 ChatGPT，其強大的基礎主要是依靠哪一種能夠卓越處理大量自然語言文法脈絡、且能夠平行化運算的網路核心架構？
> (A) CNN
> (B) GAN
> (C) Transformer
> (D) VAE
> 
> **解答**：(C)。GPT (Generative Pre-trained Transformer) 的 "T" 即代表 Transformer，它徹底顛覆了自然語言處理領域。

> [!question] 選擇題 2：
> 近年來如 Stable Diffusion 與 Midjourney 等以「輸入文字來生成超高畫質競賽級圖片」的 AI 神級繪圖工具，大多是採用下列哪一種透過逐步「去雜訊(Denoising)」來重構原圖影像的核心技術？
> (A) 擴散模型 (Diffusion Model)
> (B) 循環神經網路 (RNN)
> (C) 隱馬可夫模型
> (D) 變分自編碼器 (VAE)
> 
> **解答**：(A)。擴散模型從純粹的雜訊中一步步預測並剔除雜訊點，是目前影像生成品質的霸主。

> [!question] 選擇題 3：
> 企業想打造專屬內部客服問答系統。為了避免 ChatGPT 出現「幻覺（胡說八道）」或是「不知道公司內部最新機密」的問題，目前業界最推崇也最具成本效益的技術架構與手法是什麼？
> (A) 購買一萬張顯示卡把模型全部重訓練一次
> (B) RAG (檢索增強生成，Retrieval-Augmented Generation)
> (C) 放棄使用 LLM，改為規則式腳本 (Rule-Based)
> (D) 重新把 CNN 套用到文字上
> 
> **解答**：(B)。讓 AI 「看著公司內建的參考資料開卷考」，既解決了資訊過時，也可大幅壓低客製化訓練成本。

> [!question] 選擇題 4：
> 生成對抗網路 (GAN) 由 Generator 與 Discriminator 兩個組件互相競爭訓練而成，雖然能產出極真實的人臉，但它在工程訓練上最常遭遇什麼樣的惡性循環與痛點？
> (A) 無法輸入圖片
> (B) 模式崩潰 (Mode Collapse) 與訓練極不穩定
> (C) 無法運作於 GPU 上
> (D) 僅能處理純文字數據
> 
> **解答**：(B)。當 Generator 發現只要生成幾種特定圖案就能騙過 Discriminator 時，就會停止學習其他特徵，造成產出過度單一，這便是 Mode Collapse。

> [!question] 選擇題 5：
> 在 Transformer 之前，科學家大多使用 RNN 來處理語言。除了會忘記長文章前面的內容外，RNN 還有一個在工程運算上的致命弱點導致它無法發展成千億參數的大模型，請問是哪個弱點被 Transformer 的注意力機制解決了？
> (A) 準確率永遠無法超過 50%
> (B) RNN 必須由左至右「循序」計算，無法發揮顯示卡海量「平行運算」的優勢
> (C) RNN 占用的硬碟空間比 Transformer 大幾百倍
> (D) RNN 不能辨識英文標點符號
> 
> **解答**：(B)。注意力機制允許句子中所有的字同時進行矩陣運算，完美契合現代 GPU 極致平行運算的天賦。

> [!question] 選擇題 6：
> 如果企業堅持要在自己私有的 LLM 上「改變模型講話的整體語氣與態度」，或者注入非常極端特定領域的專業詞彙邏輯，而且不希望採用外掛字典式的 RAG，那麼較為經濟實惠的「權重修改」訓練降本方案通常會被稱為什麼？
> (A) K-Means 群聚
> (B) LoRA (Low-Rank Adaptation 等參數高效微調技術)
> (C) 全局特徵預訓練 (Grand Pre-training)
> (D) Q-Learning (強化學習)
> 
> **解答**：(B)。LoRA 等 PEFT 技術透過附加小矩陣的方法凍結龐大主體，是小企業微調大語言模型的救星。
