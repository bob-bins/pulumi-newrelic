// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "../types";

export interface AlertChannelConfig {
    /**
     * The API key for integrating with OpsGenie.
     */
    apiKey?: string;
    /**
     * Specifies an authentication password for use with a channel.  Supported by the `webhook` channel type.
     */
    authPassword?: string;
    /**
     * Specifies an authentication method for use with a channel.  Supported by the `webhook` channel type.  Only HTTP basic authentication is currently supported via the value `BASIC`.
     */
    authType?: string;
    /**
     * Specifies an authentication username for use with a channel.  Supported by the `webhook` channel type.
     */
    authUsername?: string;
    /**
     * The base URL of the webhook destination.
     */
    baseUrl?: string;
    /**
     * The Slack channel to send notifications to.
     * * `opsgenie`
     */
    channel?: string;
    /**
     * A map of key/value pairs that represents extra HTTP headers to be sent along with the webhook payload.
     */
    headers?: {[key: string]: string};
    /**
     * Use instead of `headers` if the desired payload is more complex than a list of key/value pairs (e.g. a set of headers that makes use of nested objects).  The value provided should be a valid JSON string with escaped double quotes. Conflicts with `headers`.
     */
    headersString?: string;
    /**
     * `true` or `false`. Flag for whether or not to attach a JSON document containing information about the associated alert to the email that is sent to recipients.
     * * `webhook`
     */
    includeJsonAttachment?: string;
    /**
     * The key for integrating with VictorOps.
     */
    key?: string;
    /**
     * A map of key/value pairs that represents the webhook payload.  Must provide `payloadType` if setting this argument.
     */
    payload?: {[key: string]: string};
    /**
     * Use instead of `payload` if the desired payload is more complex than a list of key/value pairs (e.g. a payload that makes use of nested objects).  The value provided should be a valid JSON string with escaped double quotes. Conflicts with `payload`.
     */
    payloadString?: string;
    /**
     * Can either be `application/json` or `application/x-www-form-urlencoded`. The `payloadType` argument is _required_ if `payload` is set.
     * * `pagerduty`
     */
    payloadType?: string;
    /**
     * A set of recipients for targeting notifications.  Multiple values are comma separated.
     */
    recipients?: string;
    /**
     * The data center region to store your data.  Valid values are `US` and `EU`.  Default is `US`.
     */
    region?: string;
    /**
     * The route key for integrating with VictorOps.
     * * `slack`
     */
    routeKey?: string;
    /**
     * Specifies the service key for integrating with Pagerduty.
     * * `victorops`
     */
    serviceKey?: string;
    /**
     * A set of tags for targeting notifications. Multiple values are comma separated.
     */
    tags?: string;
    /**
     * A set of teams for targeting notifications. Multiple values are comma separated.
     */
    teams?: string;
    /**
     * [Slack Webhook URL](https://slack.com/intl/en-es/help/articles/115005265063-Incoming-webhooks-for-Slack).
     */
    url?: string;
    userId?: string;
}

export interface AlertConditionTerm {
    duration: number;
    operator?: string;
    priority?: string;
    threshold: number;
    timeFunction: string;
}

export interface AlertMutingRuleCondition {
    /**
     * The individual MutingRuleConditions within the group. See Nested conditions blocks below for details.
     */
    conditions: outputs.AlertMutingRuleConditionCondition[];
    /**
     * The operator used to combine all the MutingRuleConditions within the group.
     */
    operator: string;
}

export interface AlertMutingRuleConditionCondition {
    /**
     * The attribute on a violation.
     */
    attribute: string;
    /**
     * The operator used to compare the attribute's value with the supplied value(s)
     */
    operator: string;
    /**
     * The value(s) to compare against the attribute's value.
     */
    values: string[];
}

export interface AlertMutingRuleSchedule {
    /**
     * The datetime stamp when the muting rule schedule stops repeating. This is in local ISO 8601 format without an offset. Example: '2020-07-10T15:00:00'. Conflicts with `repeatCount`
     */
    endRepeat?: string;
    /**
     * The datetime stamp that represents when the muting rule ends. This is in local ISO 8601 format without an offset. Example: '2020-07-15T14:30:00'
     */
    endTime?: string;
    /**
     * The frequency the muting rule schedule repeats. If it does not repeat, omit this field. Options are DAILY, WEEKLY, MONTHLY
     */
    repeat?: string;
    /**
     * The number of times the muting rule schedule repeats. This includes the original schedule. For example, a repeatCount of 2 will recur one time. Conflicts with `endRepeat`
     */
    repeatCount?: number;
    /**
     * The datetime stamp that represents when the muting rule starts. This is in local ISO 8601 format without an offset. Example: '2020-07-08T14:30:00'
     */
    startTime?: string;
    timeZone: string;
    /**
     * The day(s) of the week that a muting rule should repeat when the repeat field is set to 'WEEKLY'. Example: ['MONDAY', 'WEDNESDAY']
     */
    weeklyRepeatDays?: string[];
}

export interface DashboardFilter {
    /**
     * (Optional) A list of attributes belonging to the specified event types to enable filtering for.
     */
    attributes?: string[];
    /**
     * (Optional) A list of event types to enable filtering for.
     */
    eventTypes: string[];
}

export interface DashboardWidget {
    /**
     * (Optional) The account ID to use when querying data. If `accountId` is omitted, the widget will use the account ID associated with the API key used in your provider configuration. You can also use `accountId` to configure cross-account widgets or simply to be explicit about which account the widget will be pulling data from.
     */
    accountId?: number;
    /**
     * (Required) Column position of widget from top left, starting at `1`.
     */
    column: number;
    compareWiths?: outputs.DashboardWidgetCompareWith[];
    /**
     * (Optional) The ID of a dashboard to link to from the widget's facets.
     * * `attributeSheet`, `comparisonLineChart`, `eventFeed`, `eventTable`, `funnel`, `histogram`, `lineChart`, `rawJson`, `singleEvent`, or `uniquesList`:
     */
    drilldownDashboardId?: number;
    /**
     * (Required) The duration, in ms, of the time window represented in the chart.
     */
    duration?: number;
    /**
     * (Optional) The end time of the time window represented in the chart in epoch time.  When not set, the time window will end at the current time.
     */
    endTime?: number;
    /**
     * (Required) A collection of entity IDs to display data. These are typically application IDs.
     */
    entityIds?: number[];
    /**
     * (Optional) Can be set to "host" to facet the metric data by host.
     */
    facet?: string;
    /**
     * (Optional) Height of the widget.  Valid values are `1` to `3` inclusive.  Defaults to `1`.
     */
    height?: number;
    /**
     * (Optional) The limit of distinct data series to display.  Requires `orderBy` to be set.
     */
    limit?: number;
    /**
     * (Required) A nested block that describes a metric.  Nested `metric` blocks support the following arguments:
     */
    metrics?: outputs.DashboardWidgetMetric[];
    /**
     * (Optional) Description of the widget.
     */
    notes?: string;
    /**
     * (Required) Valid NRQL query string. See [Writing NRQL Queries](https://docs.newrelic.com/docs/insights/nrql-new-relic-query-language/using-nrql/introduction-nrql) for help.
     * * `markdown`:
     */
    nrql?: string;
    /**
     * (Optional) Set the order of the results.  Required when using `limit`.
     * * `applicationBreakdown`:
     */
    orderBy?: string;
    rawMetricName: string;
    /**
     * (Required) Row position of widget from top left, starting at `1`.
     */
    row: number;
    /**
     * (Required) The markdown source to be rendered in the widget.
     * * `metricLineChart`:
     */
    source?: string;
    /**
     * (Required) Threshold above which the displayed value will be styled with a red color.
     */
    thresholdRed?: number;
    /**
     * (Optional) Threshold above which the displayed value will be styled with a yellow color.
     * * `facetBarChart`, `facetPieChart`, `facetTable`, `facetedAreaChart`, `facetedLineChart`, or `heatmap`:
     */
    thresholdYellow?: number;
    /**
     * The title of the dashboard.
     */
    title: string;
    /**
     * (Required) How the widget visualizes data.  Valid values are `billboard`, `gauge`, `billboardComparison`, `facetBarChart`, `facetedLineChart`, `facetPieChart`, `facetTable`, `facetedAreaChart`, `heatmap`, `attributeSheet`, `singleEvent`, `histogram`, `funnel`, `rawJson`, `eventFeed`, `eventTable`, `uniquesList`, `lineChart`, `comparisonLineChart`, `markdown`, and `metricLineChart`.
     */
    visualization: string;
    widgetId: number;
    /**
     * (Optional) Width of the widget.  Valid values are `1` to `3` inclusive.  Defaults to `1`.
     */
    width?: number;
}

export interface DashboardWidgetCompareWith {
    offsetDuration: string;
    presentation: outputs.DashboardWidgetCompareWithPresentation;
}

export interface DashboardWidgetCompareWithPresentation {
    color: string;
    /**
     * (Required) The metric name to display.
     */
    name: string;
}

export interface DashboardWidgetMetric {
    /**
     * (Required) The metric name to display.
     */
    name: string;
    scope?: string;
    units?: string;
    /**
     * (Required) The metric values to display.
     */
    values?: string[];
}

export interface EntityTagsTag {
    /**
     * The tag key.
     */
    key: string;
    /**
     * The tag values.
     */
    values: string[];
}

export interface GetAlertChannelConfig {
    apiKey?: string;
    authPassword?: string;
    authType?: string;
    authUsername?: string;
    baseUrl?: string;
    channel?: string;
    headers?: {[key: string]: string};
    includeJsonAttachment?: string;
    key?: string;
    payload?: {[key: string]: string};
    payloadType?: string;
    recipients?: string;
    region?: string;
    routeKey?: string;
    serviceKey?: string;
    tags?: string;
    teams?: string;
    url?: string;
    userId?: string;
}

export interface GetEntityTag {
    key: string;
    value: string;
}

export interface InfraAlertConditionCritical {
    duration: number;
    timeFunction?: string;
    value?: number;
}

export interface InfraAlertConditionWarning {
    duration: number;
    timeFunction?: string;
    value?: number;
}

export interface NrqlAlertConditionCritical {
    /**
     * @deprecated use `threshold_duration` attribute instead
     */
    duration?: number;
    operator?: string;
    threshold: number;
    thresholdDuration?: number;
    thresholdOccurrences?: string;
    /**
     * @deprecated use `threshold_occurrences` attribute instead
     */
    timeFunction?: string;
}

export interface NrqlAlertConditionNrql {
    evaluationOffset?: number;
    query: string;
    /**
     * @deprecated use `evaluation_offset` attribute instead
     */
    sinceValue?: string;
}

export interface NrqlAlertConditionTerm {
    /**
     * @deprecated use `threshold_duration` attribute instead
     */
    duration?: number;
    operator?: string;
    priority?: string;
    threshold: number;
    thresholdDuration?: number;
    thresholdOccurrences?: string;
    /**
     * @deprecated use `threshold_occurrences` attribute instead
     */
    timeFunction?: string;
}

export interface NrqlAlertConditionWarning {
    /**
     * @deprecated use `threshold_duration` attribute instead
     */
    duration?: number;
    operator?: string;
    threshold: number;
    thresholdDuration?: number;
    thresholdOccurrences?: string;
    /**
     * @deprecated use `threshold_occurrences` attribute instead
     */
    timeFunction?: string;
}

export interface OneDashboardPage {
    /**
     * Brief text describing the dashboard.
     */
    description?: string;
    /**
     * The unique entity identifier of the dashboard page in New Relic.
     */
    guid: string;
    /**
     * The title of the dashboard.
     */
    name: string;
    /**
     * (Optional) A nested block that describes an Area widget.  See Nested widget blocks below for details.
     */
    widgetAreas?: outputs.OneDashboardPageWidgetArea[];
    /**
     * (Optional) A nested block that describes a Bar widget.  See Nested widget blocks below for details.
     */
    widgetBars?: outputs.OneDashboardPageWidgetBar[];
    /**
     * (Optional) A nested block that describes a Billboard widget.  See Nested widget blocks below for details.
     */
    widgetBillboards?: outputs.OneDashboardPageWidgetBillboard[];
    /**
     * (Optional) A nested block that describes a Bullet widget.  See Nested widget blocks below for details.
     */
    widgetBullets?: outputs.OneDashboardPageWidgetBullet[];
    /**
     * (Optional) A nested block that describes a Funnel widget.  See Nested widget blocks below for details.
     */
    widgetFunnels?: outputs.OneDashboardPageWidgetFunnel[];
    /**
     * (Optional) A nested block that describes a Heatmap widget.  See Nested widget blocks below for details.
     */
    widgetHeatmaps?: outputs.OneDashboardPageWidgetHeatmap[];
    /**
     * (Optional) A nested block that describes a Histogram widget.  See Nested widget blocks below for details.
     */
    widgetHistograms?: outputs.OneDashboardPageWidgetHistogram[];
    /**
     * (Optional) A nested block that describes a JSON widget.  See Nested widget blocks below for details.
     */
    widgetJsons?: outputs.OneDashboardPageWidgetJson[];
    /**
     * (Optional) A nested block that describes a Line widget.  See Nested widget blocks below for details.
     */
    widgetLines?: outputs.OneDashboardPageWidgetLine[];
    /**
     * (Optional) A nested block that describes a Markdown widget.  See Nested widget blocks below for details.
     */
    widgetMarkdowns?: outputs.OneDashboardPageWidgetMarkdown[];
    /**
     * (Optional) A nested block that describes a Pie widget.  See Nested widget blocks below for details.
     */
    widgetPies?: outputs.OneDashboardPageWidgetPy[];
    /**
     * (Optional) A nested block that describes a Table widget.  See Nested widget blocks below for details.
     */
    widgetTables?: outputs.OneDashboardPageWidgetTable[];
}

export interface OneDashboardPageWidgetArea {
    /**
     * (Required) Column position of widget from top left, starting at `1`.
     */
    column: number;
    /**
     * (Optional) Height of the widget.  Valid values are `1` to `12` inclusive.  Defaults to `3`.
     */
    height?: number;
    id: string;
    /**
     * (Required) A nested block that describes a NRQL Query. See Nested nrql\_query blocks below for details.
     * * `linkedEntityGuids`: (Optional) Related entity GUIDs. Currently only supports Dashboard entity GUIDs.
     */
    nrqlQueries: outputs.OneDashboardPageWidgetAreaNrqlQuery[];
    /**
     * (Required) Row position of widget from top left, starting at `1`.
     */
    row: number;
    /**
     * (Required) A title for the widget.
     */
    title: string;
    /**
     * (Optional) Width of the widget.  Valid values are `1` to `12` inclusive.  Defaults to `4`.
     */
    width?: number;
}

export interface OneDashboardPageWidgetAreaNrqlQuery {
    /**
     * Determines the New Relic account where the dashboard will be created. Defaults to the account associated with the API key used.
     */
    accountId: number;
    /**
     * (Required) Valid NRQL query string. See [Writing NRQL Queries](https://docs.newrelic.com/docs/insights/nrql-new-relic-query-language/using-nrql/introduction-nrql) for help.
     */
    query: string;
}

export interface OneDashboardPageWidgetBar {
    /**
     * (Required) Column position of widget from top left, starting at `1`.
     */
    column: number;
    /**
     * (Optional) Height of the widget.  Valid values are `1` to `12` inclusive.  Defaults to `3`.
     */
    height?: number;
    id: string;
    linkedEntityGuids?: string[];
    /**
     * (Required) A nested block that describes a NRQL Query. See Nested nrql\_query blocks below for details.
     * * `linkedEntityGuids`: (Optional) Related entity GUIDs. Currently only supports Dashboard entity GUIDs.
     */
    nrqlQueries: outputs.OneDashboardPageWidgetBarNrqlQuery[];
    /**
     * (Required) Row position of widget from top left, starting at `1`.
     */
    row: number;
    /**
     * (Required) A title for the widget.
     */
    title: string;
    /**
     * (Optional) Width of the widget.  Valid values are `1` to `12` inclusive.  Defaults to `4`.
     */
    width?: number;
}

export interface OneDashboardPageWidgetBarNrqlQuery {
    /**
     * Determines the New Relic account where the dashboard will be created. Defaults to the account associated with the API key used.
     */
    accountId: number;
    /**
     * (Required) Valid NRQL query string. See [Writing NRQL Queries](https://docs.newrelic.com/docs/insights/nrql-new-relic-query-language/using-nrql/introduction-nrql) for help.
     */
    query: string;
}

export interface OneDashboardPageWidgetBillboard {
    /**
     * (Required) Column position of widget from top left, starting at `1`.
     */
    column: number;
    /**
     * (Optional) Threshold above which the displayed value will be styled with a red color.
     */
    critical?: number;
    /**
     * (Optional) Height of the widget.  Valid values are `1` to `12` inclusive.  Defaults to `3`.
     */
    height?: number;
    id: string;
    /**
     * (Required) A nested block that describes a NRQL Query. See Nested nrql\_query blocks below for details.
     * * `linkedEntityGuids`: (Optional) Related entity GUIDs. Currently only supports Dashboard entity GUIDs.
     */
    nrqlQueries: outputs.OneDashboardPageWidgetBillboardNrqlQuery[];
    /**
     * (Required) Row position of widget from top left, starting at `1`.
     */
    row: number;
    /**
     * (Required) A title for the widget.
     */
    title: string;
    /**
     * (Optional) Threshold above which the displayed value will be styled with a yellow color.
     * * `widgetBullet`
     */
    warning?: number;
    /**
     * (Optional) Width of the widget.  Valid values are `1` to `12` inclusive.  Defaults to `4`.
     */
    width?: number;
}

export interface OneDashboardPageWidgetBillboardNrqlQuery {
    /**
     * Determines the New Relic account where the dashboard will be created. Defaults to the account associated with the API key used.
     */
    accountId: number;
    /**
     * (Required) Valid NRQL query string. See [Writing NRQL Queries](https://docs.newrelic.com/docs/insights/nrql-new-relic-query-language/using-nrql/introduction-nrql) for help.
     */
    query: string;
}

export interface OneDashboardPageWidgetBullet {
    /**
     * (Required) Column position of widget from top left, starting at `1`.
     */
    column: number;
    /**
     * (Optional) Height of the widget.  Valid values are `1` to `12` inclusive.  Defaults to `3`.
     */
    height?: number;
    id: string;
    /**
     * (Optional) Visualization limit for the widget.
     * * `widgetFunnel`
     */
    limit?: number;
    /**
     * (Required) A nested block that describes a NRQL Query. See Nested nrql\_query blocks below for details.
     * * `linkedEntityGuids`: (Optional) Related entity GUIDs. Currently only supports Dashboard entity GUIDs.
     */
    nrqlQueries: outputs.OneDashboardPageWidgetBulletNrqlQuery[];
    /**
     * (Required) Row position of widget from top left, starting at `1`.
     */
    row: number;
    /**
     * (Required) A title for the widget.
     */
    title: string;
    /**
     * (Optional) Width of the widget.  Valid values are `1` to `12` inclusive.  Defaults to `4`.
     */
    width?: number;
}

export interface OneDashboardPageWidgetBulletNrqlQuery {
    /**
     * Determines the New Relic account where the dashboard will be created. Defaults to the account associated with the API key used.
     */
    accountId: number;
    /**
     * (Required) Valid NRQL query string. See [Writing NRQL Queries](https://docs.newrelic.com/docs/insights/nrql-new-relic-query-language/using-nrql/introduction-nrql) for help.
     */
    query: string;
}

export interface OneDashboardPageWidgetFunnel {
    /**
     * (Required) Column position of widget from top left, starting at `1`.
     */
    column: number;
    /**
     * (Optional) Height of the widget.  Valid values are `1` to `12` inclusive.  Defaults to `3`.
     */
    height?: number;
    id: string;
    /**
     * (Required) A nested block that describes a NRQL Query. See Nested nrql\_query blocks below for details.
     * * `linkedEntityGuids`: (Optional) Related entity GUIDs. Currently only supports Dashboard entity GUIDs.
     */
    nrqlQueries: outputs.OneDashboardPageWidgetFunnelNrqlQuery[];
    /**
     * (Required) Row position of widget from top left, starting at `1`.
     */
    row: number;
    /**
     * (Required) A title for the widget.
     */
    title: string;
    /**
     * (Optional) Width of the widget.  Valid values are `1` to `12` inclusive.  Defaults to `4`.
     */
    width?: number;
}

export interface OneDashboardPageWidgetFunnelNrqlQuery {
    /**
     * Determines the New Relic account where the dashboard will be created. Defaults to the account associated with the API key used.
     */
    accountId: number;
    /**
     * (Required) Valid NRQL query string. See [Writing NRQL Queries](https://docs.newrelic.com/docs/insights/nrql-new-relic-query-language/using-nrql/introduction-nrql) for help.
     */
    query: string;
}

export interface OneDashboardPageWidgetHeatmap {
    /**
     * (Required) Column position of widget from top left, starting at `1`.
     */
    column: number;
    /**
     * (Optional) Height of the widget.  Valid values are `1` to `12` inclusive.  Defaults to `3`.
     */
    height?: number;
    id: string;
    /**
     * (Required) A nested block that describes a NRQL Query. See Nested nrql\_query blocks below for details.
     * * `linkedEntityGuids`: (Optional) Related entity GUIDs. Currently only supports Dashboard entity GUIDs.
     */
    nrqlQueries: outputs.OneDashboardPageWidgetHeatmapNrqlQuery[];
    /**
     * (Required) Row position of widget from top left, starting at `1`.
     */
    row: number;
    /**
     * (Required) A title for the widget.
     */
    title: string;
    /**
     * (Optional) Width of the widget.  Valid values are `1` to `12` inclusive.  Defaults to `4`.
     */
    width?: number;
}

export interface OneDashboardPageWidgetHeatmapNrqlQuery {
    /**
     * Determines the New Relic account where the dashboard will be created. Defaults to the account associated with the API key used.
     */
    accountId: number;
    /**
     * (Required) Valid NRQL query string. See [Writing NRQL Queries](https://docs.newrelic.com/docs/insights/nrql-new-relic-query-language/using-nrql/introduction-nrql) for help.
     */
    query: string;
}

export interface OneDashboardPageWidgetHistogram {
    /**
     * (Required) Column position of widget from top left, starting at `1`.
     */
    column: number;
    /**
     * (Optional) Height of the widget.  Valid values are `1` to `12` inclusive.  Defaults to `3`.
     */
    height?: number;
    id: string;
    /**
     * (Required) A nested block that describes a NRQL Query. See Nested nrql\_query blocks below for details.
     * * `linkedEntityGuids`: (Optional) Related entity GUIDs. Currently only supports Dashboard entity GUIDs.
     */
    nrqlQueries: outputs.OneDashboardPageWidgetHistogramNrqlQuery[];
    /**
     * (Required) Row position of widget from top left, starting at `1`.
     */
    row: number;
    /**
     * (Required) A title for the widget.
     */
    title: string;
    /**
     * (Optional) Width of the widget.  Valid values are `1` to `12` inclusive.  Defaults to `4`.
     */
    width?: number;
}

export interface OneDashboardPageWidgetHistogramNrqlQuery {
    /**
     * Determines the New Relic account where the dashboard will be created. Defaults to the account associated with the API key used.
     */
    accountId: number;
    /**
     * (Required) Valid NRQL query string. See [Writing NRQL Queries](https://docs.newrelic.com/docs/insights/nrql-new-relic-query-language/using-nrql/introduction-nrql) for help.
     */
    query: string;
}

export interface OneDashboardPageWidgetJson {
    /**
     * (Required) Column position of widget from top left, starting at `1`.
     */
    column: number;
    /**
     * (Optional) Height of the widget.  Valid values are `1` to `12` inclusive.  Defaults to `3`.
     */
    height?: number;
    id: string;
    /**
     * (Required) A nested block that describes a NRQL Query. See Nested nrql\_query blocks below for details.
     * * `linkedEntityGuids`: (Optional) Related entity GUIDs. Currently only supports Dashboard entity GUIDs.
     */
    nrqlQueries: outputs.OneDashboardPageWidgetJsonNrqlQuery[];
    /**
     * (Required) Row position of widget from top left, starting at `1`.
     */
    row: number;
    /**
     * (Required) A title for the widget.
     */
    title: string;
    /**
     * (Optional) Width of the widget.  Valid values are `1` to `12` inclusive.  Defaults to `4`.
     */
    width?: number;
}

export interface OneDashboardPageWidgetJsonNrqlQuery {
    /**
     * Determines the New Relic account where the dashboard will be created. Defaults to the account associated with the API key used.
     */
    accountId: number;
    /**
     * (Required) Valid NRQL query string. See [Writing NRQL Queries](https://docs.newrelic.com/docs/insights/nrql-new-relic-query-language/using-nrql/introduction-nrql) for help.
     */
    query: string;
}

export interface OneDashboardPageWidgetLine {
    /**
     * (Required) Column position of widget from top left, starting at `1`.
     */
    column: number;
    /**
     * (Optional) Height of the widget.  Valid values are `1` to `12` inclusive.  Defaults to `3`.
     */
    height?: number;
    id: string;
    /**
     * (Required) A nested block that describes a NRQL Query. See Nested nrql\_query blocks below for details.
     * * `linkedEntityGuids`: (Optional) Related entity GUIDs. Currently only supports Dashboard entity GUIDs.
     */
    nrqlQueries: outputs.OneDashboardPageWidgetLineNrqlQuery[];
    /**
     * (Required) Row position of widget from top left, starting at `1`.
     */
    row: number;
    /**
     * (Required) A title for the widget.
     */
    title: string;
    /**
     * (Optional) Width of the widget.  Valid values are `1` to `12` inclusive.  Defaults to `4`.
     */
    width?: number;
}

export interface OneDashboardPageWidgetLineNrqlQuery {
    /**
     * Determines the New Relic account where the dashboard will be created. Defaults to the account associated with the API key used.
     */
    accountId: number;
    /**
     * (Required) Valid NRQL query string. See [Writing NRQL Queries](https://docs.newrelic.com/docs/insights/nrql-new-relic-query-language/using-nrql/introduction-nrql) for help.
     */
    query: string;
}

export interface OneDashboardPageWidgetMarkdown {
    /**
     * (Required) Column position of widget from top left, starting at `1`.
     */
    column: number;
    /**
     * (Optional) Height of the widget.  Valid values are `1` to `12` inclusive.  Defaults to `3`.
     */
    height?: number;
    id: string;
    /**
     * (Required) Row position of widget from top left, starting at `1`.
     */
    row: number;
    /**
     * (Required) The markdown source to be rendered in the widget.
     * * `widgetPie`
     */
    text?: string;
    /**
     * (Required) A title for the widget.
     */
    title: string;
    /**
     * (Optional) Width of the widget.  Valid values are `1` to `12` inclusive.  Defaults to `4`.
     */
    width?: number;
}

export interface OneDashboardPageWidgetPy {
    /**
     * (Required) Column position of widget from top left, starting at `1`.
     */
    column: number;
    /**
     * (Optional) Height of the widget.  Valid values are `1` to `12` inclusive.  Defaults to `3`.
     */
    height?: number;
    id: string;
    linkedEntityGuids?: string[];
    /**
     * (Required) A nested block that describes a NRQL Query. See Nested nrql\_query blocks below for details.
     * * `linkedEntityGuids`: (Optional) Related entity GUIDs. Currently only supports Dashboard entity GUIDs.
     */
    nrqlQueries: outputs.OneDashboardPageWidgetPyNrqlQuery[];
    /**
     * (Required) Row position of widget from top left, starting at `1`.
     */
    row: number;
    /**
     * (Required) A title for the widget.
     */
    title: string;
    /**
     * (Optional) Width of the widget.  Valid values are `1` to `12` inclusive.  Defaults to `4`.
     */
    width?: number;
}

export interface OneDashboardPageWidgetPyNrqlQuery {
    /**
     * Determines the New Relic account where the dashboard will be created. Defaults to the account associated with the API key used.
     */
    accountId: number;
    /**
     * (Required) Valid NRQL query string. See [Writing NRQL Queries](https://docs.newrelic.com/docs/insights/nrql-new-relic-query-language/using-nrql/introduction-nrql) for help.
     */
    query: string;
}

export interface OneDashboardPageWidgetTable {
    /**
     * (Required) Column position of widget from top left, starting at `1`.
     */
    column: number;
    /**
     * (Optional) Height of the widget.  Valid values are `1` to `12` inclusive.  Defaults to `3`.
     */
    height?: number;
    id: string;
    linkedEntityGuids?: string[];
    /**
     * (Required) A nested block that describes a NRQL Query. See Nested nrql\_query blocks below for details.
     * * `linkedEntityGuids`: (Optional) Related entity GUIDs. Currently only supports Dashboard entity GUIDs.
     */
    nrqlQueries: outputs.OneDashboardPageWidgetTableNrqlQuery[];
    /**
     * (Required) Row position of widget from top left, starting at `1`.
     */
    row: number;
    /**
     * (Required) A title for the widget.
     */
    title: string;
    /**
     * (Optional) Width of the widget.  Valid values are `1` to `12` inclusive.  Defaults to `4`.
     */
    width?: number;
}

export interface OneDashboardPageWidgetTableNrqlQuery {
    /**
     * Determines the New Relic account where the dashboard will be created. Defaults to the account associated with the API key used.
     */
    accountId: number;
    /**
     * (Required) Valid NRQL query string. See [Writing NRQL Queries](https://docs.newrelic.com/docs/insights/nrql-new-relic-query-language/using-nrql/introduction-nrql) for help.
     */
    query: string;
}
export namespace insights {
    export interface EventEvent {
        attributes: outputs.insights.EventEventAttribute[];
        timestamp?: number;
        type: string;
    }

    export interface EventEventAttribute {
        key: string;
        type?: string;
        value: string;
    }
}

export namespace plugins {
    export interface AlertConditionTerm {
        duration: number;
        operator?: string;
        priority?: string;
        threshold: number;
        timeFunction: string;
    }

    export interface WorkloadEntitySearchQuery {
        /**
         * The query.
         */
        query: string;
    }
}

export namespace synthetics {
    export interface MultiLocationAlertConditionCritical {
        threshold: number;
    }

    export interface MultiLocationAlertConditionWarning {
        threshold: number;
    }
}
