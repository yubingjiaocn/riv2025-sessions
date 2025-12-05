async function loadSession() {
    const params = new URLSearchParams(window.location.search);
    const code = params.get('code');
    
    const response = await fetch('sessions.json');
    const data = await response.json();
    const session = data.sessions.find(s => s.session_code === code);
    
    if (!session) {
        document.body.innerHTML = '<p>Session not found</p>';
        return;
    }
    
    document.getElementById('sessionTitle').textContent = session.title_cn;
    document.getElementById('sessionAbstract').textContent = session.abstract_cn;
    
    const videoId = new URL(session.video_url).searchParams.get('v');
    document.getElementById('videoFrame').src = `https://www.youtube.com/embed/${videoId}`;
    
    const meta = document.getElementById('sessionMeta');
    meta.innerHTML = `
        <p><strong>会议代码:</strong> ${session.session_code}</p>
        <p><strong>演讲者:</strong> ${session.presenter.map(p => p.name || p).join(', ')}</p>
        <p><strong>主题:</strong> ${session.attributes.topic}</p>
        <p><strong>服务:</strong> ${session.attributes.services.join(', ')}</p>
    `;
    
    if (session.summary) {
        const summaryResp = await fetch(`sessions/${code}/summary.md`);
        const summaryText = await summaryResp.text();
        document.getElementById('summaryContent').innerHTML = marked.parse(summaryText);
    }
}

loadSession();
