// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as outputs from "../types/output";

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
     * `0` or `1`. Flag for whether or not to attach a JSON document containing information about the associated alert to the email that is sent to recipients.
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
     * Your organization's Slack URL.
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

export interface DashboardFilter {
    attributes?: string[];
    eventTypes: string[];
}

export interface DashboardWidget {
    column: number;
    compareWiths?: outputs.DashboardWidgetCompareWith[];
    drilldownDashboardId?: number;
    duration?: number;
    endTime?: number;
    entityIds?: number[];
    facet?: string;
    height?: number;
    limit?: number;
    metrics?: outputs.DashboardWidgetMetric[];
    notes?: string;
    nrql?: string;
    orderBy?: string;
    rawMetricName: string;
    row: number;
    source?: string;
    thresholdRed?: number;
    thresholdYellow?: number;
    /**
     * The title of the dashboard.
     */
    title: string;
    visualization: string;
    widgetId: number;
    width?: number;
}

export interface DashboardWidgetCompareWith {
    offsetDuration: string;
    presentation: outputs.DashboardWidgetCompareWithPresentation;
}

export interface DashboardWidgetCompareWithPresentation {
    color: string;
    name: string;
}

export interface DashboardWidgetMetric {
    name: string;
    scope?: string;
    units?: string;
    values?: string[];
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

export interface NrqlAlertConditionNrql {
    query: string;
    sinceValue: string;
}

export interface NrqlAlertConditionTerm {
    duration: number;
    operator?: string;
    priority?: string;
    threshold: number;
    timeFunction: string;
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
