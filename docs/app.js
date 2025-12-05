let sessions = [];
let allTopics = new Set();
let allServices = new Set();
let topicChoice, serviceChoice;
let pagination;
let currentFilteredSessions = [];
const itemsPerPage = 10;

async function loadSessions() {
    const response = await fetch('sessions.json');
    const data = await response.json();

    // Extract metadata and sessions
    if (data.metadata) {
        displayMetadata(data.metadata);
        sessions = data.sessions;
    } else {
        // Backward compatibility: if no metadata, assume old format
        sessions = data;
    }

    sessions.forEach(s => {
        if (s.attributes.topic) allTopics.add(s.attributes.topic);
        s.attributes.services.forEach(svc => allServices.add(svc));
    });

    populateFilters();
    currentFilteredSessions = sessions;
    renderSessions(sessions);
}

function displayMetadata(metadata) {
    // Display sessions count
    const sessionsCountEl = document.getElementById('sessionsCount');
    sessionsCountEl.textContent = `共 ${metadata.sessions_count} 场会议`;

    // Display last updated time
    const lastUpdatedEl = document.getElementById('lastUpdated');
    const updateDate = new Date(metadata.last_updated);
    const formattedDate = updateDate.toLocaleString('zh-CN', {
        year: 'numeric',
        month: '2-digit',
        day: '2-digit',
        hour: '2-digit',
        minute: '2-digit',
        timeZone: 'Asia/Shanghai'
    });
    lastUpdatedEl.textContent = `最后更新: ${formattedDate}`;
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

function renderSessions(filteredSessions, page = 1, updatePaginationControl = true) {
    const container = document.getElementById('sessionList');
    container.innerHTML = '';

    // Calculate pagination
    const startIndex = (page - 1) * itemsPerPage;
    const endIndex = startIndex + itemsPerPage;
    const paginatedSessions = filteredSessions.slice(startIndex, endIndex);

    paginatedSessions.forEach(session => {
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

    // Update pagination only when needed (not during afterMove event)
    if (updatePaginationControl) {
        updatePagination(filteredSessions.length);
    }
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

    currentFilteredSessions = filtered;
    renderSessions(filtered, 1);
}

function initPagination() {
    const container = document.getElementById('pagination');
    pagination = new tui.Pagination(container, {
        totalItems: 0,
        itemsPerPage: itemsPerPage,
        visiblePages: 5,
        page: 1,
        centerAlign: true,
        firstItemClassName: 'tui-first-child',
        lastItemClassName: 'tui-last-child'
    });

    pagination.on('afterMove', function(event) {
        renderSessions(currentFilteredSessions, event.page, false);
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });
}

function updatePagination(totalItems) {
    if (!pagination) {
        initPagination();
    }

    pagination.reset(totalItems);
}

loadSessions();
