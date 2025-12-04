let sessions = [];
let allTopics = new Set();
let allServices = new Set();
let topicChoice, serviceChoice;

async function loadSessions() {
    const response = await fetch('sessions.json');
    sessions = await response.json();

    sessions.forEach(s => {
        if (s.attributes.topic) allTopics.add(s.attributes.topic);
        s.attributes.services.forEach(svc => allServices.add(svc));
    });

    populateFilters();
    renderSessions(sessions);
}

function populateFilters() {
    const topicSelect = document.getElementById('topicFilter');
    const serviceSelect = document.getElementById('serviceFilter');

    // Populate topic options
    [...allTopics].sort().forEach(topic => {
        const option = document.createElement('option');
        option.value = topic;
        option.textContent = topic;
        topicSelect.appendChild(option);
    });

    // Populate service options
    [...allServices].sort().forEach(service => {
        const option = document.createElement('option');
        option.value = service;
        option.textContent = service;
        serviceSelect.appendChild(option);
    });

    // Initialize Choices.js
    topicChoice = new Choices(topicSelect, {
        removeItemButton: true,
        searchEnabled: true,
        searchPlaceholderValue: '搜索主题...',
        noResultsText: '未找到结果',
        noChoicesText: '无可选项',
        itemSelectText: '点击选择',
        placeholder: true,
        placeholderValue: '选择主题...'
    });

    serviceChoice = new Choices(serviceSelect, {
        removeItemButton: true,
        searchEnabled: true,
        searchPlaceholderValue: '搜索服务...',
        noResultsText: '未找到结果',
        noChoicesText: '无可选项',
        itemSelectText: '点击选择',
        placeholder: true,
        placeholderValue: '选择服务...'
    });

    // Add event listeners
    topicSelect.addEventListener('change', filterSessions);
    serviceSelect.addEventListener('change', filterSessions);
    document.getElementById('searchBox').addEventListener('input', filterSessions);
}

function renderSessions(filteredSessions) {
    const container = document.getElementById('sessionList');
    container.innerHTML = '';
    
    filteredSessions.forEach(session => {
        const card = document.createElement('div');
        card.className = 'session-card';
        card.onclick = () => window.location.href = `session.html?code=${session.session_code}`;
        
        card.innerHTML = `
            <div class="code">${session.session_code}</div>
            <h2>${session.title_cn}</h2>
            <div class="abstract">${session.abstract_cn}</div>
            <div class="tags">
                ${session.attributes.topic ? `<span class="tag">${session.attributes.topic}</span>` : ''}
                ${session.attributes.services.slice(0, 3).map(s => `<span class="tag">${s}</span>`).join('')}
            </div>
        `;
        
        container.appendChild(card);
    });
}

function filterSessions() {
    const search = document.getElementById('searchBox').value.toLowerCase();
    const selectedTopics = topicChoice.getValue(true);
    const selectedServices = serviceChoice.getValue(true);

    const filtered = sessions.filter(s => {
        const matchSearch = !search ||
            s.title_cn.toLowerCase().includes(search) ||
            s.abstract_cn.toLowerCase().includes(search) ||
            s.session_code.toLowerCase().includes(search);

        const matchTopic = selectedTopics.length === 0 ||
            selectedTopics.includes(s.attributes.topic);

        const matchService = selectedServices.length === 0 ||
            s.attributes.services.some(svc => selectedServices.includes(svc));

        return matchSearch && matchTopic && matchService;
    });

    renderSessions(filtered);
}

loadSessions();
