<template>
  <div class="card__regex-tuning">
    <h1 class="header__card-title">Regex</h1>
    <div class="item__rule_id">Rule ID: {{ ruleId }}</div>
    <div>
      <h2>Stats</h2>
      <div>
        <div>Matches</div>
        <div>4 / 50</div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: 'TuningCard'
}
</script>
<style>


.container__daemon-info code {
  background-color: var(--bg3);
  margin-left: 0;
}

.header__row-name h1 {
  font-size: 1.5em;
  margin: 0;
  font-weight: 700;
}

.card__regex-tuning {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  background-color: var(--bg3);
  width: 100%;
  padding: 0.75rem;
  border-radius: 0.25rem;
}

.header__card-title {
  font-size: 1.5em;
  font-weight: 700;
}
</style>